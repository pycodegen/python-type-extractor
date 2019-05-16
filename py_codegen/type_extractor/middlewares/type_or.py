from typing import Union

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_codegen.type_extractor.nodes.TypeOR import TypeOR


def typeor_middleware(typ, type_extractor: BaseTypeExtractor):
    typ_origin = get_typ_origin(typ)
    if typ_origin is not Union:
        return
    types = get_typ_args(typ)
    type_a = type_extractor.rawtype_to_node(types[0])
    type_b = type_extractor.rawtype_to_node(types[1])
    return TypeOR(
        a=type_a,
        b=type_b,
    )