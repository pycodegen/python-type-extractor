from dataclasses import dataclass
from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class MappingFound(BaseNodeType):  # type: ignore
    key: NodeType
    value: NodeType
