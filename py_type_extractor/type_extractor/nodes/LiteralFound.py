from dataclasses import dataclass, field
from typing import Any, Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


@dataclass
class LiteralFound(BaseNodeType):  # type: ignore
    value: Any
    options: Set[BaseOption] = field(default_factory=set)
