from collections import OrderedDict
from typing import Callable, NamedTuple, Any

class FunctionFound(NamedTuple):
    name: str
    filePath: str
    func: Callable
    raw_params: OrderedDict
    params: OrderedDict
    doc: str
    return_type: Any