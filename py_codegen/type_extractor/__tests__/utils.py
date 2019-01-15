from copy import deepcopy
from typing import Callable

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType
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
        fields = {
            key: traverse(value, func)
            for (key, value) in node.fields.items()
        }
        return func(
            node._replace(
                fields=fields
            )
        )
    if isinstance(node, FunctionFound):
        params = {
            key: traverse(value, func)
            for (key, value) in node.params.items()
        }
        return_type = traverse(node.return_type, func)
        return func(
            node._replace(
                params=params,
                return_type=return_type,
            )
        )
    if isinstance(node, TypedDictFound):
        annotations = {
            key: traverse(value, func)
            for (key, value) in node.annotations.items()
        }
        return func(
            node._replace(
                annotations=annotations,
            )
        )
    if isinstance(node, TypeOR):
        a = traverse(node.a, func)
        b = traverse(node.b, func)
        return func(
            node._replace(
                a=a,
                b=b
            )
        )
    return node


def cleanup(node: NodeType):
    if isinstance(node, ClassFound):
        new_fields = deepcopy(node.fields)

        # for python < 3.7.2 compat.
        #   (python 3.7.2 adds 'return' on fields
        new_fields.pop('return', None)
        return node._replace(
            raw_fields={},
            class_raw=None,
            fields=new_fields,
            filePath='',
            doc='',
        )

    if isinstance(node, FunctionFound):
        new_params = deepcopy(node.params)

        # for python < 3.7.2 compat.
        #   (python 3.7.2 adds 'return' on fields
        new_params.pop('return', None)
        return node._replace(
            filePath='',
            raw_params={},
            params=new_params,
            doc=None,
            func=None,  # type: ignore
        )

    if isinstance(node, TypedDictFound):
        return node._replace(
            raw=None,
        )
    return node
