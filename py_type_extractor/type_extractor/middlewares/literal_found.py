from typing import Tuple, Set

from typing_extensions import Literal

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args, remove_temp_options
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.LiteralFound import LiteralFound


def __is_literal_typ(typ_origin):
    return typ_origin == Literal \
           or (
                       hasattr(Literal, '__class__')
                       and typ_origin == Literal.__class__
               )


def literal_found_middleware(
        typ,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    child_options = remove_temp_options(options)
    typ_origin = get_typ_origin(typ)
    if not __is_literal_typ(typ_origin):
        return
    return __process_literal_args(get_typ_args(typ), child_options)


def __process_literal_args(
        args: Tuple,
        options: Set[BaseOption],
) -> LiteralFound:
    values = set()
    for typ in args:
        typ_origin = get_typ_origin(typ)
        if __is_literal_typ(typ_origin):
            typ_literal_found = __process_literal_args(
                get_typ_args(typ),
                options,
            )
            values.update(typ_literal_found.values)
        else:
            values.add(typ)
    return LiteralFound(values, options)
