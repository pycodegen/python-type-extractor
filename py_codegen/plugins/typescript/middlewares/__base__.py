from typing import Dict, List

from py_codegen.plugins.typescript.__base__ import BaseTypescriptConverter
from py_codegen.type_extractor.nodes.BaseNodeType import NodeType


def convert_params_dict(
        converter: BaseTypescriptConverter,
        node_dict: Dict[str, NodeType],
        ending: str = ','
):
    converted: List[str] = []
    for (field_name, node) in node_dict.items():
        # TODO: sanitize field_name (eg. K-S --> K_S ) ?
        converted.append(
            f"\t{field_name}: {converter.get_identifier(node)}{ending}"
        )
    return '\n'.join(converted)