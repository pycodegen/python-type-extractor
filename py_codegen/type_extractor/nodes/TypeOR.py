from dataclasses import dataclass, field
from typing import Set

from .BaseNodeType import BaseNodeType, NodeType, BaseOption


@dataclass
class TypeOR(BaseNodeType):  # type: ignore
    a: NodeType
    b: NodeType

    options: Set[BaseOption] = field(default_factory=set)
