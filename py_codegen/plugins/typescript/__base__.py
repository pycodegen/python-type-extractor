from textwrap import dedent
from typing import (
    cast,
    List,
    Dict,
    Callable)

from textwrap import (
    indent,
)

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.DictFound import DictFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.ListFound import ListFound
from py_codegen.type_extractor.nodes.NoneNode import NoneNode
from py_codegen.type_extractor.nodes.TupleFound import TupleFound
from py_codegen.type_extractor.nodes.TypeOR import TypeOR
from py_codegen.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_codegen.type_extractor.nodes.UnknownFound import unknown_found
from py_codegen.type_extractor.type_extractor import TypeExtractor, is_builtin

MiddlewareType = Callable[[
    BaseTypeExtractor,
    'BaseTypescriptConverter',
], List[str]]

class BaseTypescriptConverter:
    extractor: TypeExtractor

    middlewares: List[MiddlewareType]

    def __init__(
            self,
            extractor: TypeExtractor,
    ):
        self.extractor = extractor

    def get_identifier(self, node: NodeType) -> str:
        # TODO: sanitize names!
        if isinstance(node, NoneNode):
            return 'null'
        if isinstance(node, ClassFound):
            return node.name
        if isinstance(node, FunctionFound):
            return node.name
        if isinstance(node, TypedDictFound):
            return f"I{node.name}"
        if isinstance(node, TypeOR):
            return f"{self.get_identifier(node.a)} | {self.get_identifier(node.b)}"
        if isinstance(node, DictFound):
            return f"{{ [id: string]: {self.get_identifier(node.value)} }}"
        if isinstance(node, ListFound):
            return f"{self.get_identifier(node.typ)}[]"
        if isinstance(node, TupleFound):
            return f"[{', '.join([self.get_identifier(typ) for typ in node.types])}]"
        if node is unknown_found:
            return "any"

        if is_builtin(node):
            return self.__convert_builtin(cast(type, node))

        raise NotImplementedError(f'get_identifier not implemented for {node}')

