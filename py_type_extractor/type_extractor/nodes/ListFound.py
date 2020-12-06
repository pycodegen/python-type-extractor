from dataclasses import dataclass, field
from typing import Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.utils.get_self import get_self


@dataclass
class ListFound(BaseNodeType):  # type: ignore
    typ: NodeType

    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(get_self(self.typ)) \
               + hash(frozenset(self.options)) \
               + hash(ListFound)
