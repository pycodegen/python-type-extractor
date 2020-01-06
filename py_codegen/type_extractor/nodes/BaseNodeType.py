from dataclasses import dataclass, field
from typing import Union, Set


class BaseOption:
    pass


class BaseNodeType:
    options: Set[BaseOption]


NodeType = Union[BaseNodeType, type]

