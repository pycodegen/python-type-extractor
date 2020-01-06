from dataclasses import dataclass

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class ListFound(BaseNodeType):  # type: ignore
    typ: NodeType


