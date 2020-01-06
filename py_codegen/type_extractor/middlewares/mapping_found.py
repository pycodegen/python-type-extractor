from collections import abc
from typing import Mapping, Set

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.MappingFound import MappingFound


def mapping_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],

):
    typ_origin = get_typ_origin(typ)
    if typ_origin is not abc.Mapping and typ_origin is not Mapping:
        return
    typ_args = get_typ_args(typ)
    type_key = type_extractor.rawtype_to_node(typ_args[0])
    type_value = type_extractor.rawtype_to_node(typ_args[1])
    return MappingFound(
        key=type_key,
        value=type_value,
    )