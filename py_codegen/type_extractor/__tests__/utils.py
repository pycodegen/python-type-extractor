from collections import OrderedDict
from copy import deepcopy
from typing import Union, Callable

from py_codegen.type_extractor.ClassFound import ClassFound
from py_codegen.type_extractor.FunctionFound import FunctionFound
from py_codegen.type_extractor.TypeOR import TypeOR


def match_class_found(original: ClassFound, other: ClassFound):
    _original = sanitize_class_found(original)
    _other = sanitize_class_found(other)
    pass


def sanitize_class_found(class_found: ClassFound):
    _original = deepcopy(class_found)
    _original.filePath = ''
    _original.raw_fields = {}
    return _original


traverse_func_type = Callable[
    [Union[ClassFound, FunctionFound]],
    Union[ClassFound, FunctionFound]
]


def traverse(
        node: Union[ClassFound, FunctionFound],
        func: traverse_func_type
):
    node = deepcopy(node)
    node = func(node)
    if isinstance(node, ClassFound):
        for key, value in node.fields.items():
            if isinstance(value, TypeOR):
                value = traverseTypeOR(value, func)
            if isinstance(value, ClassFound) or isinstance(value, FunctionFound):
                value = func(value)
            node.fields[key] = value
    if isinstance(node, FunctionFound):
        for key, value in node.params.items():
            if isinstance(value, TypeOR):
                value = traverseTypeOR(value)
                node.fields[key] = value
            elif isinstance(value, ClassFound) or isinstance(value, FunctionFound):
                value = func(value)
                node.fields[key] = value
        if isinstance(node.return_type, TypeOR):
            node.return_type = traverseTypeOR(node.return_type, func)
        elif isinstance(node.return_type, ClassFound) \
                or isinstance(node.return_type, FunctionFound):
            node.return_type = func(node.return_type)
    return node


def traverseTypeOR(
        node: TypeOR,
        func: traverse_func_type,
):
    if isinstance(node.a, ClassFound) or isinstance(node.a, FunctionFound):
        node.a = func(node.a)
    if isinstance(node.a, TypeOR):
        node.a = traverseTypeOR(node.a, func)
    if isinstance(node.b, ClassFound) or isinstance(node.b, FunctionFound):
        node.b = func(node.b)
    if isinstance(node.b, TypeOR):
        node.b = traverseTypeOR(node.b, func)
    return node


def cleanup(node: Union[ClassFound, FunctionFound]):
    # try:
    if isinstance(node, ClassFound):
        new_node = deepcopy(node)
        new_node.raw_fields = OrderedDict()

        # python 3.7.2 adds 'return': None to no-return classes.
        new_node.fields.update({
            'return': new_node.fields.get('return')
        })
        new_node.filePath = ''
        new_node.doc = ''
        return new_node
    if isinstance(node, FunctionFound):
        new_node = deepcopy(node)
        new_node.filePath = ''
        new_node.raw_params = OrderedDict()
        new_node.doc = ''
        return new_node
    return node
