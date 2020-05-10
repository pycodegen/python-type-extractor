from collections import OrderedDict
from copy import deepcopy, copy
from typing import Callable

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
from py_codegen.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_codegen.type_extractor.nodes.NewType import NewTypeFound
from py_codegen.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_codegen.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.TypeOR import TypeOR


traverse_func_type = Callable[
    [NodeType],
    NodeType,
]


def traverse(node: NodeType, func: traverse_func_type):
    if isinstance(node, ClassFound):
        class_found_node = copy(node)
        class_found_node.fields = {
            key: traverse(value, func)
            for (key, value) in node.fields.items()
        }
        class_found_node.base_classes = [
            traverse(base_class, func)
            for base_class in node.base_classes
        ]
        return func(class_found_node)
    if isinstance(node, FunctionFound):
        function_found_node = copy(node)
        function_found_node.params = OrderedDict([
            (key, traverse(value, func))
            for (key, value) in node.params.items()
        ])
        function_found_node.return_type = traverse(node.return_type, func)
        return func(function_found_node)
    if isinstance(node, TypedDictFound):
        typed_dict_node = copy(node)
        typed_dict_node.annotations = {
            key: traverse(value, func)
            for (key, value) in node.annotations.items()
        }
        return func(typed_dict_node)
    if isinstance(node, TypeOR):
        typeor_node = copy(node)
        typeor_node.a = traverse(node.a, func)
        typeor_node.b = traverse(node.b, func)
        return func(typeor_node)

    if isinstance(node, FixedGenericFound):
        fixed_generic_node = copy(node)
        fixed_generic_node.origin = traverse(
            node.origin, func
        )
        fixed_generic_node.type_vars = [
            traverse(node_type_vars, func)
            for node_type_vars in node.type_vars
        ]
        return func(fixed_generic_node)

    if isinstance(node, TypeVarFound):
        typevar_node = copy(node)
        typevar_node.original = traverse(
            node.original, func
        )
        return func(typevar_node)
    if isinstance(node, NewTypeFound):
        newtype_found = copy(node)
        newtype_found.actual = traverse(
            node.actual, func
        )
        return func(newtype_found)
    return node


def cleanup(node: NodeType):
    if isinstance(node, ClassFound):
        class_found_node = copy(node)
        class_found_node.raw_fields = {}
        class_found_node.class_raw = None
        class_found_node.fields = copy(node.fields)

        # for python < 3.7.2 compat.
        #   (python 3.7.2 adds 'return' on fields
        class_found_node.fields.pop('return', None)

        class_found_node.filePath = ''
        class_found_node.doc = ''
        return class_found_node

    if isinstance(node, FunctionFound):
        new_params = copy(node.params)

        # for python < 3.7.2 compat.
        #   (python 3.7.2 adds 'return' on fields
        new_params.pop('return', None)

        func_found_node = copy(node)
        func_found_node.filePath = ''
        func_found_node.raw_params = {}
        func_found_node.params = new_params
        func_found_node.doc = ''
        func_found_node.func = None
        return func_found_node

    if isinstance(node, TypedDictFound):
        new_node = copy(node)
        new_node.raw = None
        return new_node
    return node
