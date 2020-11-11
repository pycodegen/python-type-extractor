from typing import Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from .BaseNodeType import BaseNodeType
from .BaseOption import BaseOption


class NoneNode(BaseNodeType):  # type: ignore
    def __hash__(self):
        return hash(id(NoneNode))


none_node = NoneNode()


def none_node_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if typ is type(None):
        return none_node

