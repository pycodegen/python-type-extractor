from typing import List
from textwrap import indent

from py_type_extractor.plugins.typescript.__base__ import BaseTypescriptConverter
from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.TypedDictFound import TypedDictFound

from .__base__ import (
    convert_params_dict,
)


def typeddicts_middleware(
        type_extractor: BaseTypeExtractor,
        converter: BaseTypescriptConverter,
) -> List[str]:
    classes = [
        convert_typeddict(
            typed_dict_found=value,
            converter=converter,
        )
        for (key, value)
        in type_extractor.collected_types.items()
        if isinstance(value, TypedDictFound)
    ]
    return classes


def convert_typeddict(
        typed_dict_found: TypedDictFound,
        converter: BaseTypescriptConverter,
):
    annotations = convert_params_dict(
        converter=converter,
        node_dict=typed_dict_found.annotations,
    )
    tab = '\t'
    converter = converter
    return (
        f"export interface {converter.get_identifier(typed_dict_found)} {{\n"
        f"{indent(annotations, tab)}\n"
        f"}}"
    )
