import inspect
import typing_inspect

from dataclasses import dataclass

from mypy_extensions import _TypedDictMeta  # type: ignore
from typing import Set, Dict, cast, List, Generic

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.utils import is_builtin


def is_custom_method(maybe_class_method):
    if not inspect.isfunction(maybe_class_method)\
            and not inspect.ismethod(maybe_class_method):
        return False

    try:
        inspect.getsource(maybe_class_method)
        return True

    except:
        return False


def class_found_middleware(
        _class,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not inspect.isclass(_class) \
            or is_builtin(_class) \
            or _class is inspect._empty \
            or isinstance(_class, _TypedDictMeta):
        return None

    duplicate = type_extractor.collected_types.get(_class.__name__)
    if duplicate is not None:
        assert isinstance(duplicate, ClassFound) \
               and duplicate.class_raw == _class
        duplicate.options = duplicate.options.union(options)
        return duplicate
    _data_class = dataclass(_class)

    base_classes = cast(List[ClassFound], [
        type_extractor.rawtype_to_node(base_cls)
        for base_cls in list(_class.__bases__)
        if base_cls is not object and
           base_cls is not tuple and
           base_cls is not Generic
    ])

    argspec = inspect.getfullargspec(_data_class)
    module = inspect.getmodule(_class)
    filename = module and module.__file__
    annotations: Dict = getattr(_class, '__annotations__', argspec.annotations)
    fields = type_extractor.params_to_nodes(annotations, annotations.keys())
    type_vars = [
        type_extractor.rawtype_to_node(_typevar)
        for _typevar in
        list(typing_inspect.get_parameters(_class))
    ]
    custom_methods_raw = inspect.getmembers(_class, predicate=is_custom_method)
    custom_methods = {
        name: type_extractor.rawtype_to_node(method)
        for (name, method) in custom_methods_raw
    }
    class_found = ClassFound(
        name=_class.__name__,
        class_raw=_class,
        filePath=filename,
        base_classes=base_classes,
        raw_fields=argspec.annotations,
        custom_methods=custom_methods,
        fields=fields,
        doc=_class.__doc__,
        options=options,
        type_vars=type_vars,
    )

    type_extractor.collected_types[class_found.name] = class_found
    return class_found
