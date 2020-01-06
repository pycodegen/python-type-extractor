from dataclasses import dataclass
from typing import Any

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType


@dataclass
class LiteralFound(BaseNodeType):  # type: ignore
    value: Any
