import inspect

from dataclasses import dataclass

from mypy_extensions import _TypedDictMeta  # type: ignore
from typing import Set

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.utils import is_builtin


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
    base_classes = [
        type_extractor.rawtype_to_node(base_cls)
        for base_cls in list(_class.__bases__)
        if base_cls is not object and base_cls is not tuple
    ]
    argspec = inspect.getfullargspec(_data_class)
    module = inspect.getmodule(_class)
    filename = module and module.__file__
    fields = type_extractor.params_to_nodes(argspec.annotations, argspec.args)
    # methods = [
    #     type_extractor.rawtype_to_node(method)
    #     for (name, method) in inspect.getmembers(_class, predicate=inspect.isfunction)
    #     and not name.
    # ]
    methods = [
        # type_extractor.rawtype_to_node(method, )
        (name, method)
        for name, method in inspect.getmembers(_class, predicate=inspect.isfunction)
        if name.startswith('__')
    ]
    class_found = ClassFound(
        name=_class.__name__,
        class_raw=_class,
        filePath=filename,
        base_classes=base_classes,
        raw_fields=argspec.annotations,
        fields=fields,
        doc=_class.__doc__,
        options=options,
    )

    type_extractor.collected_types[class_found.name] = class_found
    return class_found
