from typing import List

from py_codegen.plugins.typescript.__base__ import BaseTypescriptConverter
from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.ClassFound import ClassFound

from .__base__ import (
    convert_params_dict,
)


def class_middleware(
        type_extractor: BaseTypeExtractor,
        converter: BaseTypescriptConverter,
) -> List[str]:
    classes = [
        convert_class(
            class_found=value,
            converter=converter,
        )
        for (key, value)
        in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    ]
    return classes


def convert_class(
        class_found: ClassFound,
        converter: BaseTypescriptConverter,
):
    fields = convert_params_dict(
        converter=converter,
        node_dict=class_found.fields,
        ending=';',
    )
    return (
        f"export class {converter.get_identifier(class_found)} {{\n"
        f"   {fields} \n"
        "}"
    )