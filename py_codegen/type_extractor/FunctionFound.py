from collections import OrderedDict
from typing import Callable, NamedTuple, Any
from dataclasses import dataclass

@dataclass(
    order=True,
)
class FunctionFound:
    name: str
    filePath: str
    func: Callable
    raw_params: OrderedDict
    params: OrderedDict
    doc: str
    return_type: Any