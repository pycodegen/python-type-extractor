from typing import Dict

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_codegen.type_extractor.nodes.DictFound import DictFound


def dict_found_middleware(typ, type_extractor: BaseTypeExtractor):
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