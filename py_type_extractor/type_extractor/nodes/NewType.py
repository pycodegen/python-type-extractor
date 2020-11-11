from dataclasses import dataclass, field
from typing import List, Any, Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


@dataclass
class NewTypeFound(BaseNodeType):
    name: str
    actual: NodeType
    original_ref: Any = None

    options: Set[BaseOption] = field(default_factory=set)
    # TODO: bug in python? can't get module_name for NewType...
    # module_name: str = field(default='')

    def __hash__(self):
        return hash(id(NewTypeFound)) \
               + hash(self.name) \
               + hash(id(self.original_ref))