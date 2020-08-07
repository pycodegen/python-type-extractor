from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType


class DuplicateNameFound(Exception):
    def __init__(
        self,
        found1: NodeType,
        found2: NodeType,
    ):
        pass
