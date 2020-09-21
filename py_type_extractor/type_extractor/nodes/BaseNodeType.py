from dataclasses import dataclass, field
from typing import Union, Set


class BaseOption:
    pass


class BaseNodeType:
    options: Set[BaseOption]

    # for de-referencing weakref.proxy
    def get_self(self):
        return self


NodeType = Union[BaseNodeType, type]

