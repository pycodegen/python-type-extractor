import inspect

from dataclasses import dataclass

from mypy_extensions import _TypedDictMeta  # type: ignore

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.utils import is_builtin


def class_found_middleware(_class, type_extractor: BaseTypeExtractor):
    if not inspect.isclass(_class) \
            or is_builtin(_class) \
            or _class is inspect._empty \
            or isinstance(_class, _TypedDictMeta):
        return None
    _data_class = dataclass(_class)
    argspec = inspect.getfullargspec(_data_class)
    module = inspect.getmodule(_class)
    filename = module and module.__file__
    fields = type_extractor.params_to_nodes(argspec.annotations, argspec.args)
    class_found = ClassFound(
        name=_class.__name__,
        class_raw=_class,
        filePath=filename,
        raw_fields=argspec.annotations,
        fields=fields,
        doc=_class.__doc__
    )
    duplicate = type_extractor.collected_types.get(class_found.name)
    assert duplicate == class_found or duplicate is None

    type_extractor.collected_types[class_found.name] = class_found
    return class_found
