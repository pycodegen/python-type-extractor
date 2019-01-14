from typing import Dict, NamedTuple, Optional

from mypy_extensions import _TypedDictMeta  # type: ignore

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


class TypedDictFound(NamedTuple, BaseNodeType):  # type: ignore
    annotations: Dict[str, NodeType]
    name: str = ''
    raw: Optional[_TypedDictMeta] = None
