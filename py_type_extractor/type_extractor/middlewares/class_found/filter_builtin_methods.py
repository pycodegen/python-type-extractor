import inspect
from typing import Tuple, Any


def filter_builtin_methods(method: Tuple[str, Any]):
    (name, maybe_func) = method
    if name.startswith('__'):
        return False
    if not inspect.isfunction(maybe_func):
        return False
    return True