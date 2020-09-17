from dataclasses import dataclass
from typing import Set, Dict, List, Optional, TypeVar, Any
#
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType, BaseOption


@dataclass
class TypeVarFound(BaseNodeType):
    name: str
    original: TypeVar  # type:ignore
    type_limits: Optional[List[NodeType]] = None
