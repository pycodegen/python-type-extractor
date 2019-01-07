from collections import OrderedDict
from typing import Callable, NamedTuple, Any, Optional, Dict
from dataclasses import dataclass


@dataclass(
    order=True,
)
class FunctionFound:
    name: str
    filePath: str
    func: Callable
    raw_params: Dict[str, Any]
    params: OrderedDict
    doc: Optional[str]
    return_type: Any
    __params_extra: Optional[Dict[str, OrderedDict]] = None
    __return_type_extra: Optional[Dict[str, Any]] = None


def set_params_extra(namespace: str):
    def __set_fields_extra(
            func_found: FunctionFound,
            params_extra: OrderedDict,
    ):
        func_found.__params_extra = func_found.__params_extra or {}

        func_found.__params_extra[namespace] = params_extra
    return __set_fields_extra


def get_params_extra(namespace: str) -> Callable[[FunctionFound], Optional[Dict[str, Any]]]:
    def __get_params_extra(func_found: FunctionFound):
        return func_found.__params_extra and \
               func_found.__params_extra.get(namespace)
    return __get_params_extra


def set_return_type_extra(namespace: str) -> Callable[[FunctionFound, Any], None]:
    def __set_return_type_extra(func_found: FunctionFound, extra: Any):
        func_found.__return_type_extra = func_found.__return_type_extra or {}
        func_found.__return_type_extra[namespace] = extra

    return __set_return_type_extra


def get_return_type_extra(namespace: str) -> Callable[[FunctionFound], Optional[Any]]:
    def __get_return_type_extra(func_found: FunctionFound):
        return func_found.__return_type_extra and \
               func_found.__return_type_extra.get(namespace)
    return __get_return_type_extra
