from typing import Tuple, Set
from typing_extensions import Literal

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import get_typ_origin, get_typ_args
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseOption
from py_type_extractor.type_extractor.nodes.LiteralFound import LiteralFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR


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
    typ_origin = get_typ_origin(typ)
    if not __is_literal_typ(typ_origin):
        return
    return __process_literal_args(get_typ_args(typ))


def __process_literal_args(args: Tuple):
    current = LiteralFound(args[0])
    if __is_literal_typ(get_typ_origin(args[0])):
        current = __process_literal_args(get_typ_args(args[0]))
    if len(args) == 1:
        return current
    return TypeOR(current, __process_literal_args(args[1:]))
