from typing import (
    Optional,
    Dict,
    Any,
    Callable,
    NamedTuple,
)

from py_codegen.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType


class ClassFound(BaseNodeType, NamedTuple):  # type: ignore
    name: str
    fields: Dict[str, NodeType]
    filePath: str = ''
    raw_fields: Dict[str, Any] = {}
    doc: str = ''
    class_raw: Optional[type] = None
    INTERNAL_fields_extra: Optional[Dict[str, Any]] = None


def set_fields_extra(namespace: str):
    def __set_fields_extra(
            class_found: ClassFound,
            extra: Dict[str, Any],
    ):
        fields_extra = class_found.INTERNAL_fields_extra or {}
        fields_extra[namespace] = extra
        return class_found._replace(
            INTERNAL_fields_extra=fields_extra,
        )
    return __set_fields_extra


def get_fields_extra(
        namespace: str,
) -> Callable[[ClassFound], Optional[Dict[str, Any]]]:
    def __get_fields_extra(class_found: ClassFound):
        return class_found.INTERNAL_fields_extra \
               and class_found.INTERNAL_fields_extra.get(namespace)
    return __get_fields_extra
