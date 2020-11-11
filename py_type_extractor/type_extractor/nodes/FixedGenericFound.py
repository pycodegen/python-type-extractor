from dataclasses import dataclass, field
from typing import List, Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


@dataclass
class FixedGenericFound(BaseNodeType):
    type_vars: List[NodeType]
    origin: NodeType
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(id(FixedGenericFound))\
               + hash(tuple(self.type_vars))\
               + hash(self.origin)
