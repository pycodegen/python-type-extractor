from typing import List, Set

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.ListFound import ListFound


def list_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    typ_origin = get_typ_origin(typ)
    if typ_origin is not list and typ_origin is not List:
        return
    typ_args = get_typ_args(typ)
    processed_typ = type_extractor.rawtype_to_node(typ_args[0])
    return ListFound(typ=processed_typ)