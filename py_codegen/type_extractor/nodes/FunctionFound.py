from dataclasses import dataclass, field
from typing import Callable, Any, Optional, Dict

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class FunctionFound(BaseNodeType):
    name: str
    params: Dict[str, NodeType]
    return_type: Any
    func: Optional[Callable] = None
    raw_params: Dict[str, Any] = field(default_factory=dict)
    doc: str = ''
    filePath: str = ''
    INTERNAL_params_extra: Optional[Dict[str, Dict[str, Any]]] = None
    INTERNAL_return_extra: Optional[Dict[str, Any]] = None


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
