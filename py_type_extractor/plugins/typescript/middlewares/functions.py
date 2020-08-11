from typing import List

from py_type_extractor.plugins.typescript.__base__ import BaseTypescriptConverter
from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.NoneNode import none_node
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from .__base__ import (
    convert_params_dict,
)


def functionfounds_middleware(
        type_extractor: BaseTypeExtractor,
        converter: BaseTypescriptConverter,
) -> List[str]:
    classes = [
        convert_functionfound(
            func_found=value,
            converter=converter,
        )
        for (key, value)
        in type_extractor.collected_types.items()
        if isinstance(value, FunctionFound)
    ]
    return classes


def convert_functionfound(
        func_found: FunctionFound,
        converter: BaseTypescriptConverter,
):
    raw_params = {
        key: value if key not in func_found.default_values
        else TypeOR(a=value, b=none_node)
        for (key, value) in func_found.params.items()
    }
    params = convert_params_dict(
        converter=converter,
        node_dict=raw_params,
        ending=',',
    )
    return (
        f"export function {converter.get_identifier(func_found)}(\n"
        f"    {params}\n"
        f"): {converter.get_identifier(func_found.return_type)}"
    )
