from typing import Dict, Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.DictFound import DictFound
from py_type_extractor.type_extractor.nodes.UnknownFound import unknown_found


def dict_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if typ == Dict:  # for `Dict`
        return DictFound(
            key=unknown_found,
            value=unknown_found,
            options=options,
        )
    typ_origin = get_typ_origin(typ)
    if typ_origin is not dict and typ_origin is not Dict:
        return

    typ_args = get_typ_args(typ)
    processed_key_typ = type_extractor.rawtype_to_node(typ_args[0])
    processed_value_typ = type_extractor.rawtype_to_node(typ_args[1])
    return DictFound(
        key=processed_key_typ,
        value=processed_value_typ,
    )
