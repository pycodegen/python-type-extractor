from dataclasses import dataclass, field
from typing import Set, Dict, List, Optional, TypeVar, Any
#
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


@dataclass
class TypeVarFound(BaseNodeType):
    name: str
    original: TypeVar  # type:ignore
    type_limits: Optional[List[NodeType]] = None
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(TypeVarFound)\
               + hash(self.name)\
               + hash(id(self.original)) \
               + hash(tuple(self.type_limits or []))
