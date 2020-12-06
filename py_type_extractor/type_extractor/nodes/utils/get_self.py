from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType, BaseNodeType


def get_self(node: NodeType):
    if isinstance(node, BaseNodeType):
        return node.get_self()
    return node
