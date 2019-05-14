from typing import List

from py_codegen.plugins.typescript.__base__ import BaseTypescriptConverter
from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound

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
    params = convert_params_dict(
        converter=converter,
        node_dict=func_found.params,
        ending=',',
    )
    return (
        f"export function {converter.get_identifier(func_found)}(\n"
        f"    {params}\n"
        f"): {converter.get_identifier(func_found.return_type)}"
    )