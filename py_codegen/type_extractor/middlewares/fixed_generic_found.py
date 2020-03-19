from typing import Dict, Set
import typing_inspect

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption


def fixed_generic_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    # if not typing_inspect.is_generic_type(typ) \
    #         or typing_inspect.get_origin(typ) is typ:
    #     return None

    if not typing_inspect.is_generic_type(typ):
        return None

    origin = typing_inspect.get_origin(typ)

    if origin is typ:
        return None

    origin_node = type_extractor.rawtype_to_node(origin)
    type_vars = [
        type_extractor.rawtype_to_node(raw_type)
        for raw_type in typing_inspect.get_args(typ)
    ]
    return FixedGenericFound(
        type_vars=type_vars,
        origin=origin_node,
    )