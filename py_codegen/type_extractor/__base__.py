from abc import ABC
from typing import Dict, Union, List

from py_codegen.type_extractor.nodes.BaseNodeType import NodeType


class BaseTypeExtractor(ABC):
    collected_types: Dict[str, NodeType]

    def __init__(self):
        self.collected_types = dict()

    def params_to_nodes(
            self,
            params: Dict[str, Union[type, None]],
            param_names_list: List[str],
    ) -> Dict[str, NodeType]:
        pass

    def rawtype_to_node(self, typ) -> NodeType:
        pass

    def add(self, options=None):
        def add_decoration(typ):
            pass
        return add_decoration
