from dataclasses import dataclass, field
from typing import (
    Optional,
    Dict,
    Any,
    Callable,
)

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


@dataclass
class ClassFound(BaseNodeType):  # type: ignore
    name: str
    fields: Dict[str, NodeType]
    filePath: str = field(default='')
    raw_fields: Dict[str, Any] = field(default_factory=dict)
    doc: str = field(default='')
    class_raw: Optional[type] = None
    INTERNAL_fields_extra: Optional[Dict[str, Any]] = None


def set_fields_extra(namespace: str):
    def __set_fields_extra(
            class_found: ClassFound,
            extra: Dict[str, Any],
    ):
        class_found.INTERNAL_fields_extra = \
            class_found.INTERNAL_fields_extra or {}

        class_found.INTERNAL_fields_extra[namespace] = \
            extra
        return class_found
    return __set_fields_extra


def get_fields_extra(
        namespace: str,
) -> Callable[[ClassFound], Optional[Dict[str, Any]]]:
    def __get_fields_extra(class_found: ClassFound):
        return class_found.INTERNAL_fields_extra \
               and class_found.INTERNAL_fields_extra.get(namespace)
    return __get_fields_extra
