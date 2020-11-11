import inspect
import weakref
from typing import Set, Dict, cast, List, Generic, Union, NamedTuple, Tuple, Callable, Any
from optparse import OptionParser

import typing_inspect
from dataclasses import dataclass
from mypy_extensions import _TypedDictMeta  # type: ignore

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.__flags import FromMethod
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_type_extractor.type_extractor.utils import is_builtin


def filter_builtin_methods(method: Tuple[str, Any]):
    (name, maybe_func) = method
    if name.startswith('__'):
        return False
    if not inspect.isfunction(maybe_func):
        return False
    return True

def class_found_middleware(
        _class,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not inspect.isclass(_class) \
            or is_builtin(_class) \
            or _class is inspect._empty \
            or isinstance(_class, _TypedDictMeta):  # type: ignore
        return None

    module = inspect.getmodule(_class)
    module_name = module.__name__

    name = _class.__qualname__.replace('.<locals>', '')
    collected_types_key = type_extractor.to_collected_types_key(
        module_name=module_name,
        typ_name=name,
    )
    duplicate = type_extractor.collected_types.get(collected_types_key)
    if duplicate is not None:
        assert isinstance(duplicate, ClassFound) \
               and duplicate.class_raw == _class
        duplicate.options = duplicate.options.union(options)
        return duplicate

    _data_class = dataclass(_class)

    base_classes_raw = typing_inspect.get_generic_bases(_class)

    base_classes = cast(
        List[Union[ClassFound, FixedGenericFound]],
        [
            type_extractor.rawtype_to_node(_parent_class)
            for _parent_class in base_classes_raw
            if typing_inspect.get_origin(_parent_class) is not Generic  # type: ignore
            and _parent_class is not NamedTuple
        ],
    )

    if len(base_classes_raw) == 0:
        base_classes = cast(List[Union[ClassFound, FixedGenericFound]], [
            type_extractor.rawtype_to_node(base_cls)
            for base_cls in list(_class.__bases__)
            if base_cls is not object and
               base_cls is not tuple and
               base_cls is not Generic  # type: ignore
        ])

    argspec = inspect.getfullargspec(_data_class)

    filename = module and module.__file__ or ''

    # methods_raw = inspect.getmembers(_class, filter_builtin_methods)
    raw_methods_with_builtins = cast(
        List[Tuple[str, Callable]],
        inspect.getmembers(_class, inspect.isfunction),
    )

    class_found = ClassFound(
        name=name,
        class_raw=_class,
        filePath=filename,
        base_classes=base_classes,
        raw_fields=argspec.annotations,
        methods={},
        fields={},
        type_vars=[],
        module_name=module_name,
        # fields=fields,
        doc=_class.__doc__,
        options=options,
        # type_vars=type_vars,
    )

    type_extractor.collected_types[collected_types_key] = class_found

    _annotations: Dict = getattr(_class, '__annotations__', argspec.annotations)
    annotations = {
        key: value if type(value) is not str
        else getattr(module, value)
        for (key, value) in _annotations.items()
    }

    fields = type_extractor.params_to_nodes(
        annotations,
        cast(List[str], annotations.keys()),
    )
    type_vars = cast(
        List[TypeVarFound],
        [
            type_extractor.rawtype_to_node(_typevar)
            for _typevar in
            list(typing_inspect.get_parameters(_class))
        ]
    )

    methods: Dict[str, FunctionFound] = {
        method_name: type_extractor.rawtype_to_node(
            func, {
                FromMethod(
                    method_name=method_name,
                ),
            },
        )
        for method_name, func in raw_methods_with_builtins
        if not method_name.startswith('__')
    }

    class_found.fields = fields
    class_found.type_vars = type_vars
    class_found.methods = methods

    return weakref.proxy(class_found)
