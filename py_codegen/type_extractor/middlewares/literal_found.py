from typing import Tuple
from typing_extensions import Literal

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.LiteralFound import LiteralFound
from py_codegen.type_extractor.nodes.TypeOR import TypeOR


def literal_found_middleware(typ, type_extractor: BaseTypeExtractor):
    typ_origin = typ.__origin__
    if typ_origin is not Literal:
        return
    return __process_literal_args(typ.__args__)


def __process_literal_args(args: Tuple):
    current = LiteralFound(args[0])
    try:
        if args[0].__origin__ is Literal:
            current = __process_literal_args(args[0].__args__)
    except:
        pass
    if len(args) == 1:
        return current
    return TypeOR(current, __process_literal_args(args[1:]))
