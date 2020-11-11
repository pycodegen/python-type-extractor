from typing import Union, Set

from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


class BaseNodeType:
    options: Set[BaseOption]

    # for de-referencing weakref.proxy
    def get_self(self):
        return self


NodeType = Union[BaseNodeType, type]

