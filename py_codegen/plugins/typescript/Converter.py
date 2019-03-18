from textwrap import dedent
from typing import (
    cast,
    List,
    Dict,
)

from textwrap import (
    indent,
)

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.DictFound import DictFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.ListFound import ListFound
from py_codegen.type_extractor.nodes.NoneNode import NoneNode
from py_codegen.type_extractor.nodes.TypeOR import TypeOR
from py_codegen.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_codegen.type_extractor.nodes.UnknownFound import unknown_found
from py_codegen.type_extractor.type_extractor import TypeExtractor, is_builtin


class TypescriptConverter:
    extractor: TypeExtractor

    def __init__(
            self,
            extractor: TypeExtractor,
    ):
        self.extractor = extractor

    def get_identifier(self, node: NodeType) -> str:
        # TODO: sanitize names!
        # import pdb;pdb.set_trace()
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
        if node is unknown_found:
            return "any"

        # import pdb;pdb.set_trace()
        if is_builtin(node):
            return self.__convert_builtin(cast(type, node))

        raise NotImplementedError(f'get_identifier not implemented for {node}')

    def run(self):

        result: List[str] = []
        for (key, class_found) in self.extractor.classes.items():
            result.append(self.convert_class_found(class_found))

        for (key, function_found) in self.extractor.functions.items():
            result.append(self.convert_functions_found(function_found))

        for (key, typed_dict_found) in self.extractor.typed_dicts.items():
            result.append(self.convert_typed_dict_found(typed_dict_found))

        return '\n'.join(result)

    def __convert_builtin(self, typ: type):
        if typ == str:
            return 'string'
        if typ == int or typ == float:
            return 'number'

    def __convert_node_dict(self, node_dict: Dict[str, NodeType], ending: str = ','):
        converted: List[str] = []
        for (field_name, node) in node_dict.items():
            # TODO: sanitize field_name (eg. K-S --> K_S ) ?
            converted.append(
                f"\t{field_name}: {self.get_identifier(node)}{ending}"
            )
        return '\n'.join(converted)

    def convert_class_found(self, class_found: ClassFound):
        return (
            f"export class {self.get_identifier(class_found)} {{\n"
            f"   {self.__convert_node_dict(class_found.fields, ';')} \n"
            "}"
        )

    def convert_functions_found(self, function_found: FunctionFound):
        return (
            f"export function {self.get_identifier(function_found)}(\n"
            f"    {self.__convert_node_dict(function_found.params)}\n"
            f"): {self.get_identifier(function_found.return_type)}"
        )

    def convert_typed_dict_found(self, typed_dict_found: TypedDictFound):
        annotations = self.__convert_node_dict(typed_dict_found.annotations)
        tab = '\t'
        return (
            f"export interface {self.get_identifier(typed_dict_found)} {{\n"
            f"{indent(annotations, tab)}\n"
            f"}}"
        )
