import abc
from typing import Optional, Set

from py_type_extractor.type_extractor.__tests__.utils.traverse_func_type import TraverseFuncType
from py_type_extractor.type_extractor.__tests__.utils.flags.__base__ import BaseUtilFlag
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


class BaseTraversableOption(
    BaseOption,
    metaclass=abc.ABCMeta,
):
    from py_type_extractor.type_extractor.__tests__.utils.traversed_or_traversing import TraversedOrTraversing
    @abc.abstractmethod
    def traverse(
            self,
            func: TraverseFuncType,
            already_traversed: TraversedOrTraversing = None,
            flags: Optional[Set[BaseUtilFlag]] = None,
    ) -> 'BaseTraversableOption':
        pass