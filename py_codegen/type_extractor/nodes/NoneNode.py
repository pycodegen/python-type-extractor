from typing import NamedTuple

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from .BaseNodeType import BaseNodeType


class NoneNode(NamedTuple, BaseNodeType):  # type: ignore
    pass


none_node = NoneNode()


def none_node_middleware(typ, type_extractor: BaseTypeExtractor):
    if typ is type(None):
        return none_node

