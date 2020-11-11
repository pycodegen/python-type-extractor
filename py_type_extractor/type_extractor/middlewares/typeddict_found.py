import inspect
import weakref

from mypy_extensions import _TypedDictMeta  # type: ignore
from typing import Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.TypedDictFound import TypedDictFound


def typeddict_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not isinstance(typ, _TypedDictMeta):
        return

    module = inspect.getmodule(typ)
    module_name = module.__name__
    name = typ.__qualname__

    collected_types_key = type_extractor.to_collected_types_key(
        module_name=module_name,
        typ_name=name,
    )

    already_processed_node = type_extractor.collected_types.get(collected_types_key)
    if already_processed_node:
        return already_processed_node

    annotations = {
        key: type_extractor.rawtype_to_node(value)
        for key, value in typ.__annotations__.items()
    }
    typed_dict_found = TypedDictFound(
        annotations=annotations,
        module_name=module_name,
        name=typ.__qualname__,
        raw=typ,
        options=options,
    )
    type_extractor.collected_types[collected_types_key] = typed_dict_found

    return weakref.proxy(typed_dict_found)
