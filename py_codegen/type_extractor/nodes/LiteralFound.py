from typing import NamedTuple, Any

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType


class LiteralFound(NamedTuple, BaseNodeType):  # type: ignore
    value: Any
