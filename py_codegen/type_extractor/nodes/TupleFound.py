from typing import NamedTuple, List

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


class TupleFound(NamedTuple, BaseNodeType):  # type: ignore
    types: List[NodeType]
