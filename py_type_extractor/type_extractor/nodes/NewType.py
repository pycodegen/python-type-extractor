from dataclasses import dataclass
from typing import List

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class NewTypeFound(BaseNodeType):
    name: str
    actual: NodeType
