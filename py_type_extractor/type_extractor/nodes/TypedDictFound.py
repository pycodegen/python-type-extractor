from dataclasses import dataclass, field
from typing import Dict, Optional, Set
from typing_extensions import _TypedDictMeta  # type: ignore

# from mypy_extensions import _TypedDictMeta  # type: ignore

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType, BaseOption


@dataclass
class TypedDictFound(BaseNodeType):  # type: ignore
    annotations: Dict[str, NodeType]
    name: str = ''
    raw: Optional[_TypedDictMeta] = None
    options: Set[BaseOption] = field(default_factory=set)
