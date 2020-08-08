import itertools
from typing import (
    cast,
    List,
    Callable,
    Any,
    Optional,
)
from typing_extensions import Protocol

from py_type_extractor.plugins.typescript.__base__ import MiddlewareType
from py_type_extractor.plugins.typescript.middlewares.classes import class_middleware
from py_type_extractor.plugins.typescript.middlewares.functions import functionfounds_middleware
from py_type_extractor.plugins.typescript.middlewares.typeddicts import typeddicts_middleware
from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.DictFound import DictFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.ListFound import ListFound
from py_type_extractor.type_extractor.nodes.LiteralFound import LiteralFound
from py_type_extractor.type_extractor.nodes.MappingFound import MappingFound
from py_type_extractor.type_extractor.nodes.NoneNode import NoneNode
from py_type_extractor.type_extractor.nodes.TupleFound import TupleFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from py_type_extractor.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_type_extractor.type_extractor.nodes.UnknownFound import unknown_found
from py_type_extractor.type_extractor.type_extractor import TypeExtractor, is_builtin


class LiteralConverterType(Protocol):
    def __call__(self, val: Any) -> str: ...


def default_literal_converter(val: Any) -> str:
    if isinstance(val, str):
        return f"'{val}'"

    if val is True:
        return "true"
    if val is False:
        return "false"
    if isinstance(val, int) \
            or isinstance(val, float):
        return f"{val}"
    if isinstance(val, list):
        converted = [default_literal_converter(item) for item in val]
        converted_str = ','.join(converted)
        return f"[{converted_str}]"
    if val is None:
        return "null"
    raise NotImplementedError(f"default_literal_converter cannot handle {val}")


class TypescriptConverter:
    extractor: TypeExtractor
    middlewares: List[MiddlewareType]
    literal_converter: LiteralConverterType

    def __init__(
            self,
            extractor: TypeExtractor,
            middlewares: Optional[List[MiddlewareType]] = None,
            literal_converter: LiteralConverterType = default_literal_converter,
    ):
        self.extractor = extractor
        self.middlewares = middlewares or [
            class_middleware,
            functionfounds_middleware,
            typeddicts_middleware,
        ]
        self.literal_converter = literal_converter

    def get_identifier(self, node: NodeType) -> str:
        # TODO: sanitize names!
        if isinstance(node, NoneNode):
            return 'null'
        if isinstance(node, ClassFound):
            return node.name.replace('.', '__')
        if isinstance(node, FunctionFound):
            return node.name.replace('.', '__')
        if isinstance(node, TypedDictFound):
            return f"I{node.name}"
        if isinstance(node, TypeOR):
            return f"{self.get_identifier(node.a)} | {self.get_identifier(node.b)}"
        # FIXME: need to handle type(key) == int / float / etc.
        if isinstance(node, DictFound):
            return f"{{ [id: string]: {self.get_identifier(node.value)} }}"
        if isinstance(node, MappingFound):
            return f"{{ [id: string]: {self.get_identifier(node.value)} }}"
        if isinstance(node, ListFound):
            return f"{self.get_identifier(node.typ)}[]"
        if isinstance(node, TupleFound):
            return f"[{', '.join([self.get_identifier(typ) for typ in node.types])}]"
        if isinstance(node, LiteralFound):
            return self.literal_converter(node.value)
        if node is unknown_found:
            return "any"

        if is_builtin(node):
            return self.__convert_builtin(cast(type, node))

        raise NotImplementedError(f'get_identifier not implemented for {node}')

    def __convert_builtin(self, typ: type):
        if typ == str:
            return 'string'
        if typ == int or typ == float:
            return 'number'
        if typ == bool:
            return 'boolean'

        raise NotImplementedError(f'__convert_builtin not implemented for {typ}')

    def run(self):
        r: List[List[str]] = [
            middleware(self.extractor, self)
            for middleware in self.middlewares
        ]
        merged: List[str] = list(itertools.chain.from_iterable(r))
        return '\n'.join(merged)


