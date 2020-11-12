from typing import Set

import typing_inspect

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound


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

    if origin is typ \
            or origin is None:
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
