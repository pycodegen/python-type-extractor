from typing import Union, Set
import typing_inspect
from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import (
    get_typ_origin,
    get_typ_args,
)
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
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
    nodes: Set[NodeType] = set()
    for typ in types:
        converted_typ = type_extractor.rawtype_to_node(typ, options)
        if isinstance(converted_typ, TypeOR):
            nodes.update(converted_typ.nodes)
        else:
            nodes.add(converted_typ)
    return TypeOR(
        nodes=nodes,
    )
