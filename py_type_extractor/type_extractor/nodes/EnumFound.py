from dataclasses import dataclass, field
from typing import (
    Optional,
    Dict,
    Any,
    Callable,
    Set, List, Union,
)

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType, BaseOption
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound

EnumValueTypes = Union[int, str]

@dataclass
class EnumFound(BaseNodeType):  # type: ignore
    name: str
    members: Dict[str, EnumValueTypes]
    filePath: str = field(default='')
    module_name: str = field(default='')
    doc: str = field(default='')
    enum_raw: Optional[type] = None
    INTERNAL_fields_extra: Optional[Dict[str, Any]] = None
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(id(EnumFound)) + hash(self.name) + hash(self.module_name)


def set_fields_extra(namespace: str):
    def __set_fields_extra(
            enum_found: EnumFound,
            extra: Dict[str, Any],
    ):
        enum_found.INTERNAL_fields_extra = \
            enum_found.INTERNAL_fields_extra or {}

        enum_found.INTERNAL_fields_extra[namespace] = \
            extra
        return enum_found
    return __set_fields_extra


def get_fields_extra(
        namespace: str,
) -> Callable[[EnumFound], Optional[Dict[str, Any]]]:
    def __get_fields_extra(enum_found: EnumFound):
        return enum_found.INTERNAL_fields_extra \
               and enum_found.INTERNAL_fields_extra.get(namespace)
    return __get_fields_extra
