from dataclasses import dataclass

from .BaseNodeType import BaseNodeType, NodeType


@dataclass
class TypeOR(BaseNodeType):  # type: ignore
    a: NodeType
    b: NodeType
