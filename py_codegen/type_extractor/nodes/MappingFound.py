from typing import NamedTuple

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


class MappingFound(NamedTuple, BaseNodeType):  # type: ignore
    key: NodeType
    value: NodeType
