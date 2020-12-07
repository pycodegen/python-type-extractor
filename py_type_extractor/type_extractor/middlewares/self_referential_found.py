from typing import Set

import typing_inspect

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.SelfReferentialFound import SelfReferentialFound


def self_referential_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not typing_inspect.is_forward_ref(typ):
        return None
    name = typing_inspect.get_forward_arg(typ)
    return SelfReferentialFound(
        name=name,
        options=options,
    )

