from dataclasses import dataclass, field
from typing import List, Any

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class NewTypeFound(BaseNodeType):
    name: str
    actual: NodeType
    original_ref: Any = None
    # TODO: bug in python? can't get module_name for NewType...
    # module_name: str = field(default='')

    def __hash__(self):
        return hash(id(NewTypeFound)) \
               + hash(self.name) \
               + hash(id(self.original_ref))