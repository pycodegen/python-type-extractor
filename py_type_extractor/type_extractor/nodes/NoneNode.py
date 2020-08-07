from typing import Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from .BaseNodeType import BaseNodeType, BaseOption


class NoneNode(BaseNodeType):  # type: ignore
    pass


none_node = NoneNode()


def none_node_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if typ is type(None):
        return none_node

