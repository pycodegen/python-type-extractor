import builtins
import inspect
from collections import (
    OrderedDict,
)
from typing import (
    Callable,
    Dict,
    Union,
    List,
    Any,
)

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.middlewares.class_found import class_found_middleware
from py_codegen.type_extractor.middlewares.dict_found import dict_found_middleware
from py_codegen.type_extractor.middlewares.function_found import func_found_middleware
from py_codegen.type_extractor.middlewares.list_found import list_found_middleware
from py_codegen.type_extractor.middlewares.mapping_found import mapping_found_middleware
from py_codegen.type_extractor.middlewares.tuple_found import tuple_found_middleware
from py_codegen.type_extractor.middlewares.type_or import typeor_middleware
from py_codegen.type_extractor.nodes.BaseNodeType import NodeType, BaseNodeType
from py_codegen.type_extractor.nodes.NoneNode import none_node_middleware
from py_codegen.type_extractor.middlewares.typeddict_found import typeddict_found_middleware
from py_codegen.type_extractor.nodes.UnknownFound import unknown_found


def is_builtin(typ):
    return inspect.getmodule(typ) is builtins


def builtin_middleware(typ, type_extractor: 'TypeExtractor'):
    if is_builtin(typ):
        return typ


class TypeExtractor(BaseTypeExtractor):
    middlewares: List[
        Callable[
            [Any, 'TypeExtractor'],
            BaseNodeType,
        ]
    ] = [
        list_found_middleware,
        typeor_middleware,
        typeddict_found_middleware,
        dict_found_middleware,
        tuple_found_middleware,
        class_found_middleware,
        func_found_middleware,
        mapping_found_middleware,
        none_node_middleware,
        builtin_middleware,
        typeddict_found_middleware,
    ]

    collected_types: Dict[str, NodeType]

    def __init__(self):
        self.functions = dict()
        self.classes = dict()
        self.typed_dicts = dict()
        BaseTypeExtractor.__init__(self)

    def params_to_nodes(
            self,
            params: Dict[str, Union[type, None]],
            param_names_list: List[str],
    ):
        processed_params: OrderedDict[str, NodeType] = OrderedDict()
        banned_words = [
            'self', 'return', '_cls',
        ]
        _param_names_list = filter(lambda name: name not in banned_words, param_names_list)
        for param_name in _param_names_list:
            processed_params[param_name] = self.rawtype_to_node(
                params.get(param_name) or inspect._empty,  # type: ignore
            )
        return processed_params

    # def rawtype_to_node(self, typ):

    def rawtype_to_node(self, typ, options=None):
        for middleware in self.middlewares:
            # noinspection PyBroadException
            try:
                value = middleware(typ, self)
                if value is not None:
                    return value
            except Exception as e:
                pass
        return unknown_found

        # if typ is inspect._empty:
        #     return unknown_found
        #
        # elif inspect.isfunction(typ):
        #     function_found = self.__to_function_found(typ)
        #     return function_found
        #
        # elif inspect.isclass(typ):
        #     class_found = self.__to_class_found(typ)
        #     self.__add_found(class_found)
        #     return class_found
        #
        # return unknown_found

        # raise NotImplementedError(f'type_extractor not implemented for {typ}')

    def add(self, options=None):
        def add_decoration(typ):
            if not is_builtin(typ):
                self.rawtype_to_node(typ, options)
            return typ
        return add_decoration