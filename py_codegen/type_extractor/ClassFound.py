from dataclasses import dataclass
from typing import Optional, Dict, Any, Callable, NewType, Union

_FieldsExtra = NewType('_FieldsExtra', Dict[str, Any])


@dataclass(
    order=True,
)
class ClassFound:
    name: str
    filePath: str
    raw_fields: Dict[str, Any]
    fields: Dict[str, Union[type, None]]
    doc: str
    class_raw: Optional[type] = None
    __fields_extra: Optional[Dict[str, Any]] = None


def set_fields_extra(namespace: str):
    def __set_fields_extra(class_found: ClassFound, fields_extra: Dict[str, Any]):
        class_found.__fields_extra = class_found.__fields_extra or {}
        class_found.__fields_extra[namespace] = fields_extra
    return __set_fields_extra


def get_fields_extra(namespace: str) -> Callable[[ClassFound], Optional[Dict[str, Any]]]:
    def __get_fields_extra(class_found: ClassFound):
        return class_found.__fields_extra and class_found.__fields_extra.get(namespace)
    return __get_fields_extra
