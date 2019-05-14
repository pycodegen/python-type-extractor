from typing import List

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.ListFound import ListFound


def list_found_middleware(typ, type_extractor: BaseTypeExtractor):
    typ_origin = typ.__origin__
    if typ_origin is not list and typ_origin is not List:
        return
    processed_typ = type_extractor.rawtype_to_node(typ.__args__[0])
    return ListFound(typ=processed_typ)