from copy import copy
from typing import Set

from py_type_extractor.type_extractor.__tests__.utils.flags.KeepClassMethods import KeepClassMethods, keep_class_methods
from py_type_extractor.type_extractor.__tests__.utils.flags.__base__ import BaseUtilFlag
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.EnumFound import EnumFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.TypedDictFound import TypedDictFound


def cleanup(
        node: NodeType,
        flags: Set[BaseUtilFlag] = None,
):
    if flags is None:
        flags = set()

    if isinstance(node, ClassFound):
        class_found_node = copy(node)
        class_found_node.raw_fields = {}
        class_found_node.class_raw = None
        class_found_node.fields = copy(node.fields)
        if keep_class_methods in flags:
            class_found_node.methods = copy(node.methods)
        else:
            class_found_node.methods = {}

        # for python < 3.7.2 compat.
        #   (python 3.7.2 adds 'return' on fields
        class_found_node.fields.pop('return', None)

        class_found_node.filePath = ''
        class_found_node.doc = ''
        return class_found_node

    if isinstance(node, EnumFound):
        enum_found_node = copy(node)
        enum_found_node.enum_raw = None
        enum_found_node.filePath = ''
        return enum_found_node

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