from typing import Set, TypeVar, Callable

from py_type_extractor.type_extractor.__tests__.utils.flags.__base__ import BaseUtilFlag
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType

TNode = TypeVar('TNode', bound=NodeType)


TraverseFuncType = Callable[[TNode, Set[BaseUtilFlag]], TNode]
