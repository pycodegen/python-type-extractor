from typing import (
    Optional,
    Dict,
    Any,
    Callable,
    NewType,
    Union,
    NamedTuple,
)

_FieldsExtra = NewType('_FieldsExtra', Dict[str, Any])


class ClassFound(NamedTuple):
    name: str
    fields: Dict[str, Union[type, None]]
    filePath: str = ''
    raw_fields: Dict[str, Any] = {}
    doc: str = ''
    class_raw: Optional[type] = None
    INTERNAL_fields_extra: Optional[Dict[str, Any]] = None


def set_fields_extra(namespace: str):
    def __set_fields_extra(
            class_found: ClassFound,
            fields_extra: Dict[str, Any],
    ):
        class_found.INTERNAL_fields_extra = \
            class_found.INTERNAL_fields_extra or {}
        class_found.INTERNAL_fields_extra[namespace] = fields_extra
    return __set_fields_extra


def get_fields_extra(
        namespace: str,
) -> Callable[[ClassFound], Optional[Dict[str, Any]]]:
    def __get_fields_extra(class_found: ClassFound):
        return class_found.INTERNAL_fields_extra \
               and class_found.INTERNAL_fields_extra.get(namespace)
    return __get_fields_extra
