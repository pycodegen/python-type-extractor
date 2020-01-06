from dataclasses import dataclass, field
from typing import Set

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType, BaseOption


@dataclass
class MappingFound(BaseNodeType):  # type: ignore
    key: NodeType
    value: NodeType

    options: Set[BaseOption] = field(default_factory=set)
