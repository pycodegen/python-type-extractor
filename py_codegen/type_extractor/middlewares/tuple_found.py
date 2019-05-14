from typing import Tuple

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.TupleFound import TupleFound


def tuple_found_middleware(typ, type_extractor: BaseTypeExtractor):
    typ_origin = typ.__origin__
    if typ_origin is not tuple and typ_origin is not Tuple:
        return
    processed_typ = [
        type_extractor.rawtype_to_node(param)
        for param in typ.__args__
    ]
    return TupleFound(types=processed_typ)