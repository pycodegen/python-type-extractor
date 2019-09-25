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
        _field_name = field_name if field_name.isidentifier() else f"'{field_name}'"
        converted.append(
            f"\t{_field_name}: {converter.get_identifier(node)}{ending}"
        )
    return '\n'.join(converted)