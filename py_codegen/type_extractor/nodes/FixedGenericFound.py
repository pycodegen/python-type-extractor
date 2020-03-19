from dataclasses import dataclass
from typing import List

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class FixedGenericFound(BaseNodeType):
    type_vars: List[NodeType]
    origin: NodeType