from dataclasses import dataclass, field
from typing import List, Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


# note: this is mostly 'temporary' node
@dataclass
class SelfReferentialFound(BaseNodeType):
    name: str
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(self.name) + id(SelfReferentialFound)