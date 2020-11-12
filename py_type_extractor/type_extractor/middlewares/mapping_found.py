from collections import abc
from typing import Mapping, Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args, remove_temp_options
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.MappingFound import MappingFound


def mapping_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],

):
    child_options = remove_temp_options(options)
    typ_origin = get_typ_origin(typ)
    if typ_origin is not abc.Mapping and typ_origin is not Mapping:
        return
    typ_args = get_typ_args(typ)
    type_key = type_extractor.rawtype_to_node(
        typ_args[0],
        options=child_options,
    )
    type_value = type_extractor.rawtype_to_node(
        typ_args[1],
        options=child_options,
    )
    return MappingFound(
        key=type_key,
        value=type_value,
        options=options,
    )
