from typing import Tuple, Set

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.TupleFound import TupleFound


def tuple_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    typ_origin = get_typ_origin(typ)
    if typ_origin is not tuple and typ_origin is not Tuple:
        return
    typ_args = get_typ_args(typ)
    processed_typ = [
        type_extractor.rawtype_to_node(param)
        for param in typ_args
    ]
    return TupleFound(types=processed_typ)