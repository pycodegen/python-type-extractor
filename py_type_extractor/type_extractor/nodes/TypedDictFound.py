from dataclasses import dataclass, field
from typing import Dict, Optional, Set

try:
    from typing_extensions import _TypedDictMeta  # type: ignore
except:
    from mypy_extensions import _TypedDictMeta  # type: ignore


from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType, BaseOption


@dataclass
class TypedDictFound(BaseNodeType):  # type: ignore
    annotations: Dict[str, NodeType]
    name: str = field(default='')
    module_name: str = field(default='')
    raw: Optional[_TypedDictMeta] = field(default=None)
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        # exclude annotations: TypedDictA --> TypedDictB --> TypedDictA
        return hash(id(TypedDictFound)) + hash(self.name) + hash(self.module_name)
