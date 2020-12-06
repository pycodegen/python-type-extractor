from dataclasses import dataclass, field
from typing import List, Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.utils.get_self import get_self


@dataclass
class FixedGenericFound(BaseNodeType):
    type_vars: List[NodeType]
    origin: NodeType
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(id(FixedGenericFound))\
               + hash(frozenset([
                    get_self(i)
                    for i in self.type_vars
                 ]))\
               + hash(get_self(self.origin))
