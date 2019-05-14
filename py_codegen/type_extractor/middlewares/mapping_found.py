from collections import abc
from typing import Mapping

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.MappingFound import MappingFound


def mapping_found_middleware(typ, type_extractor: BaseTypeExtractor):
    typ_origin = typ.__origin__
    if typ_origin is not abc.Mapping and typ_origin is not Mapping:
        return
    type_key = type_extractor.rawtype_to_node(typ.__args__[0])
    type_value = type_extractor.rawtype_to_node(typ.__args__[1])
    return MappingFound(
        key=type_key,
        value=type_value,
    )