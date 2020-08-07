from abc import ABC
from textwrap import dedent
from typing import (
    cast,
    List,
    Dict,
    Callable)

from textwrap import (
    indent,
)

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.DictFound import DictFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.ListFound import ListFound
from py_type_extractor.type_extractor.nodes.NoneNode import NoneNode
from py_type_extractor.type_extractor.nodes.TupleFound import TupleFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from py_type_extractor.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_type_extractor.type_extractor.nodes.UnknownFound import unknown_found
from py_type_extractor.type_extractor.type_extractor import TypeExtractor, is_builtin

MiddlewareType = Callable[
    [BaseTypeExtractor, 'BaseTypescriptConverter'],
    List[str],
]

class BaseTypescriptConverter(ABC):
    extractor: TypeExtractor

    middlewares: List[MiddlewareType]

    def __init__(
            self,
            extractor: TypeExtractor,
    ):
        ...

    def get_identifier(self, node: NodeType) -> str:
        ...



