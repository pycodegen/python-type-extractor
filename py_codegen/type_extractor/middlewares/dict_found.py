from typing import Dict

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.DictFound import DictFound


def dict_found_middleware(typ, type_extractor: BaseTypeExtractor):
    typ_origin = typ.__origin__
    if typ_origin is not dict and typ_origin is not Dict:
        return
    processed_key_typ = type_extractor.rawtype_to_node(typ.__args__[0])
    processed_value_typ = type_extractor.rawtype_to_node(typ.__args__[1])
    return DictFound(
        key=processed_key_typ,
        value=processed_value_typ,
    )