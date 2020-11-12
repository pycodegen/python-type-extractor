import abc
from typing import Dict, Union, List, Set, Optional

from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption


class BaseTypeExtractor(metaclass=abc.ABCMeta):
    collected_types: Dict[str, NodeType]

    def __init__(self):
        self.collected_types = dict()

    @staticmethod
    def to_collected_types_key(module_name, typ_name):
        return f"{module_name}___{typ_name}"

    @abc.abstractmethod
    def params_to_nodes(
            self,
            params: Dict[str, Union[type, None]],
            param_names_list: List[str],
            options: Optional[Set[BaseOption]] = None,
    ) -> Dict[str, NodeType]:
        pass

    @abc.abstractmethod
    def rawtype_to_node(
            self, typ,
            options: Optional[Set[BaseOption]] = None,
    ) -> NodeType:
        pass

    def add(
            self,
            options: Optional[Set[BaseOption]] = None,
    ):
        def add_decoration(typ):
            pass
        return add_decoration
