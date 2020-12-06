from typing import Dict, Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.__tests__.utils.traverse_node import traverse
from py_type_extractor.type_extractor.__tests__.utils.flags.__base__ import BaseUtilFlag
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType


def hash_test(type_extractor: BaseTypeExtractor):
    for (key, value) in type_extractor.collected_types.items():
        traverse(value, _hash_test)


def _hash_test(
        node: NodeType,
        flags: Set[BaseUtilFlag] = None,
):
    try:
        hashed = hash(node)
        print('hashing:', node)
        print('output: ', hashed)
        return node
    except Exception as e:
        raise RuntimeError(f"Hash failed -- couldn't hash ", node)
#
# def hash_test(type_extractor: BaseTypeExtractor):
#     # maybe: do recursive-hash testing?
#
#     for (key, value) in type_extractor.collected_types.items():
#         try:
#             hashed = hash(value)
#             print('hashed: ', value, 'output: ', hashed)
#         except Exception as e:
#             raise RuntimeError(f"Hash failed -- couldn't hash {key} of {value}")