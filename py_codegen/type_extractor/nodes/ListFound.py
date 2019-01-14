from typing import NamedTuple

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


class ListFound(NamedTuple, BaseNodeType):  # type: ignore
    typ: NodeType
