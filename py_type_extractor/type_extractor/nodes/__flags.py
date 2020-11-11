from dataclasses import dataclass

from py_type_extractor.type_extractor.nodes.BaseOption import BaseTempOption


@dataclass(frozen=True)
class FromMethod(
    BaseTempOption,
):
    method_name: str