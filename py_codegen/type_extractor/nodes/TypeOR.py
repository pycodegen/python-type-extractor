from typing import NamedTuple
from .BaseNodeType import BaseNodeType


class TypeOR(NamedTuple, BaseNodeType):  # type: ignore
    a: type
    b: type
