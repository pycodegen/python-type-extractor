from dataclasses import dataclass, field
from typing import (
    Optional,
    Dict,
    Any,
    Callable,
    Set, List, Union,
)

from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseNodeType, NodeType
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound


@dataclass
class ClassFound(BaseNodeType):  # type: ignore
    name: str
    fields: Dict[str, NodeType]
    filePath: str = field(default='')
    module_name: str = field(default='')
    raw_fields: Dict[str, Any] = field(default_factory=dict)
    methods: Dict[str, FunctionFound] = field(default_factory=dict)
    doc: str = field(default='')
    base_classes: List[Union[FixedGenericFound, 'ClassFound']] = field(default_factory=list)
    type_vars: List[TypeVarFound] = field(default_factory=list)
    class_raw: Optional[type] = None
    INTERNAL_fields_extra: Optional[Dict[str, Any]] = None
    options: Set[BaseOption] = field(default_factory=set)

    def __hash__(self):
        return hash(id(ClassFound)) + hash(self.name) + hash(self.module_name)


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
