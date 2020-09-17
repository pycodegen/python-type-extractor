import inspect

from typing import Set
from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
import typing_inspect

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

    already_found = type_extractor.collected_types.get(typ.__name__)
    if already_found:
        return already_found

    newtype_found = NewTypeFound(
        name=typ.__name__,
        actual=type_extractor.rawtype_to_node(typ.__supertype__),
        original_ref=typ,
    )

    type_extractor.collected_types[typ.__name__] = newtype_found
    return newtype_found
