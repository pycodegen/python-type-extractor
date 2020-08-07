import inspect

from typing import Set
from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseOption
from py_type_extractor.type_extractor.nodes.NewType import NewTypeFound


def newtype_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not inspect.isfunction(typ):
        return None
    if typ.__module__ is not 'typing':
        return None
    if typ.__code__.co_name is not 'new_type':
        return None

    newtype_found = NewTypeFound(
        name=typ.__name__,
        actual=type_extractor.rawtype_to_node(typ.__supertype__),
    )

    type_extractor.collected_types[newtype_found.name] = newtype_found
    return newtype_found
