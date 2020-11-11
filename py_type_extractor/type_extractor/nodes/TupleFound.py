from dataclasses import dataclass, field
from typing import List, Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


@dataclass
class TupleFound(BaseNodeType):
    types: List[NodeType]
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(id(TupleFound)) + hash(tuple(self.types))