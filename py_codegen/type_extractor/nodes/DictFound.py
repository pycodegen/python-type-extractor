from typing import NamedTuple

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


class DictFound(NamedTuple, BaseNodeType):  # type: ignore

    key: NodeType
    value: NodeType
