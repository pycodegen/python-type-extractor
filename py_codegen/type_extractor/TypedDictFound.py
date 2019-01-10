from typing import Dict, NamedTuple, Union, Optional

from mypy_extensions import _TypedDictMeta

from py_codegen.type_extractor.ClassFound import ClassFound
from py_codegen.type_extractor.FunctionFound import FunctionFound


class TypedDictFound(NamedTuple):
    annotations: Dict[str, Union[type, FunctionFound, ClassFound]]
    name: str = ''
    raw: Optional[_TypedDictMeta] = None
