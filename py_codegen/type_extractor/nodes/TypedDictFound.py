from dataclasses import dataclass
from typing import Dict, Optional
from typing_extensions import _TypedDictMeta  # type: ignore

# from mypy_extensions import _TypedDictMeta  # type: ignore

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class TypedDictFound(BaseNodeType):  # type: ignore
    annotations: Dict[str, NodeType]
    name: str = ''
    raw: Optional[_TypedDictMeta] = None

