from dataclasses import dataclass, field
from typing import Callable, Any, Optional, Dict, Set

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType, BaseOption


@dataclass
class FunctionFound(BaseNodeType):
    name: str
    params: Dict[str, NodeType]
    return_type: Any
    func: Optional[Callable] = None
    default_values: Dict[str, Any] = field(default_factory=dict)
    raw_params: Dict[str, Any] = field(default_factory=dict)
    module_name: str = field(default='')
    doc: str = ''
    filePath: str = ''
    INTERNAL_params_extra: Optional[Dict[str, Dict[str, Any]]] = None
    INTERNAL_return_extra: Optional[Dict[str, Any]] = None
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(FunctionFound)\
               + hash(self.name)\
               + hash(self.module_name)


def set_params_extra(namespace: str):
    def __set_fields_extra(
            func_found: FunctionFound,
            extra: Dict[str, Any],
    ):
        func_found.INTERNAL_params_extra = \
            func_found.INTERNAL_params_extra or {}
        func_found.INTERNAL_params_extra[namespace] = extra
        return func_found

    return __set_fields_extra


def get_params_extra(
        namespace: str
) -> Callable[[FunctionFound], Optional[Dict[str, Any]]]:
    def __get_params_extra(func_found: FunctionFound):
        return func_found.INTERNAL_params_extra and \
               func_found.INTERNAL_params_extra.get(namespace)
    return __get_params_extra


def set_return_type_extra(
        namespace: str
) -> Callable[[FunctionFound, Any], None]:
    def __set_return_type_extra(func_found: FunctionFound, extra: Any):
        func_found.INTERNAL_return_extra = \
            func_found.INTERNAL_return_extra or {}
        func_found.INTERNAL_return_extra[namespace] = extra
        return func_found

    return __set_return_type_extra


def get_return_type_extra(
        namespace: str
) -> Callable[[FunctionFound], Optional[Any]]:
    def __get_return_type_extra(func_found: FunctionFound):
        return func_found.INTERNAL_return_extra and \
               func_found.INTERNAL_return_extra.get(namespace)
    return __get_return_type_extra
