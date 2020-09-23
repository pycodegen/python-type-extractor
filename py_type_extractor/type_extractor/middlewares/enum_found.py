import enum
import inspect
import weakref
from typing import Set, Dict

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseOption
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.EnumFound import EnumFound, EnumValueTypes
from py_type_extractor.type_extractor.utils.items_view_to_iterable import items_view_to_iterable


def enum_found_middleware(
        _typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not inspect.isclass(_typ) \
            or not issubclass(_typ, enum.Enum):
        return None

    module = inspect.getmodule(_typ)
    module_name = module.__name__

    name = _typ.__qualname__.replace('.<locals>', '')
    collected_types_key = type_extractor.to_collected_types_key(
        module_name=module_name,
        typ_name=name,
    )
    duplicate = type_extractor.collected_types.get(collected_types_key)
    if duplicate is not None:
        assert isinstance(duplicate, ClassFound) \
               and duplicate.class_raw == _typ
        duplicate.options = duplicate.options.union(options)
        return duplicate

    filename = (module and module.__file__) or ''

    members: Dict[str, EnumValueTypes] = {
        key: enum_member.value
        for (key, enum_member) in items_view_to_iterable(_typ.__members__.items())
    }
    enum_found = EnumFound(
        name=name,
        enum_raw=_typ,
        filePath=filename,
        members=members,
        module_name=module_name,
        doc=_typ.__doc__,
        options=options,
    )

    type_extractor.collected_types[collected_types_key] = enum_found
    return weakref.proxy(enum_found)
