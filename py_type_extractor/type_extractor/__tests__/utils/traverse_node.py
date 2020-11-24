from collections import OrderedDict
from copy import copy
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from typing import Any, Set, TypeVar, cast

from py_type_extractor.type_extractor.__tests__.utils.traverse_func_type import TraverseFuncType
from py_type_extractor.type_extractor.__tests__.utils.flags.KeepClassMethods import keep_class_methods
from py_type_extractor.type_extractor.__tests__.utils.flags.__base__ import BaseUtilFlag
from py_type_extractor.type_extractor.__tests__.utils.traversed_or_traversing import TraversedOrTraversing
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
from py_type_extractor.type_extractor.nodes.BaseTraversableOption import BaseTraversableOption
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.EnumFound import EnumFound
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.NewType import NewTypeFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_type_extractor.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_type_extractor.type_extractor.nodes.UnknownFound import INTERNAL___UnknownFound


TNode = TypeVar('TNode', bound=NodeType)


def traverse(
        node: TNode,
        func: TraverseFuncType,
        already_traversed: TraversedOrTraversing = None,
        flags: Set[BaseUtilFlag] = None,
) -> TNode:
    if already_traversed is None:
        already_traversed = dict()
    if type(already_traversed) == set:
        print('aaa')
    if flags is None:
        flags = set()

    if isinstance(node, INTERNAL___UnknownFound):
        return node

    if not isinstance(node, BaseNodeType):
        return node
    # node = cast(BaseNodeType, node.get_self())
    node_id = id(node)
    if node_id in already_traversed:
        return cast(
            Any,
            already_traversed[node_id],
        )

    new_options: Set[BaseOption] = set([
        opt.traverse(func, already_traversed, flags)
        if isinstance(opt, BaseTraversableOption)
        else opt
        for opt in list(node.options)
    ])

    if isinstance(node, EnumFound):
        enum_found_node = func(copy(node), flags)
        already_traversed[node_id] = enum_found_node
        enum_found_node.options = new_options
        return enum_found_node
    if isinstance(node, ClassFound):
        class_found_node = func(copy(node), flags)
        already_traversed[node_id] = class_found_node
        class_found_node.fields = {
            key: traverse(value, func, already_traversed, flags)
            for key, value in node.fields.items()
        }
        class_found_node.base_classes = [
            traverse(base_class, func, already_traversed, flags)
            for base_class in node.base_classes
        ]
        class_found_node.options = new_options
        if keep_class_methods in flags:
            class_found_node.methods = {
                key: traverse(
                    value, func, already_traversed, flags,
                )
                for key, value in node.methods.items()
            }
        return class_found_node
    if isinstance(node, FunctionFound):
        function_found_node = func(copy(node), flags)
        already_traversed[node_id] = function_found_node
        function_found_node.params = OrderedDict([
            (key, traverse(value, func, already_traversed, flags))
            for (key, value) in node.params.items()
        ])
        function_found_node.return_type = traverse(
            node.return_type,
            func,
            already_traversed,
            flags,
        )
        function_found_node.options = new_options
        return function_found_node

    if isinstance(node, TypedDictFound):
        typed_dict_node = func(copy(node), flags)
        already_traversed[node_id] = typed_dict_node
        typed_dict_node.annotations = {
            key: traverse(value, func, already_traversed, flags)
            for (key, value) in node.annotations.items()
        }
        typed_dict_node.options = new_options
        return typed_dict_node

    if isinstance(node, TypeOR):
        typeor_node = func(copy(node), flags)
        already_traversed[node_id] = typeor_node
        typeor_node.nodes = set([
            traverse(node_item, func, already_traversed, flags)
            for node_item in list(node.nodes)
        ])
        typeor_node.options = new_options
        return typeor_node

    if isinstance(node, FixedGenericFound):
        fixed_generic_node = func(copy(node), flags)
        already_traversed[node_id] = fixed_generic_node
        fixed_generic_node.origin = traverse(
            node.origin, func, already_traversed, flags,
        )
        fixed_generic_node.type_vars = [
            traverse(node_type_vars, func, already_traversed, flags)
            for node_type_vars in node.type_vars
        ]
        fixed_generic_node.options = new_options
        return fixed_generic_node

    if isinstance(node, TypeVarFound):
        typevar_node = func(copy(node), flags)
        already_traversed[node_id] = typevar_node
        typevar_node.options = new_options
        return typevar_node

    if isinstance(node, NewTypeFound):
        newtype_found = func(copy(node), flags)
        already_traversed[node_id] = newtype_found
        newtype_found.actual = traverse(
            node.actual, func, already_traversed, flags,
        )
        newtype_found.options = new_options
        return newtype_found
    return node