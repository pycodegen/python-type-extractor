from typing import Union, Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR


def typeor_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
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
