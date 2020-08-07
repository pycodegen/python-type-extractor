import typing_inspect
from typing import Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseOption
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound


def typevar_found_middleware(
        _typevar,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not typing_inspect.is_typevar(_typevar):
        return None
    # __typevar = cast(TypeVar, _typevar)
    return TypeVarFound(
        name=_typevar.__name__,
        original=_typevar,
    )
