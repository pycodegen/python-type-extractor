from dataclasses import dataclass, field
from typing import Any, Set

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, BaseOption


@dataclass
class LiteralFound(BaseNodeType):  # type: ignore
    value: Any
    options: Set[BaseOption] = field(default_factory=set)
