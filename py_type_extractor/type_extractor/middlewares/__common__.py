from typing import Set

from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption, BaseTempOption


def get_typ_origin(typ):
    return getattr(typ, '__origin__', getattr(typ, '__class__', None))


def get_typ_args(typ):
    return getattr(typ, '__args__', getattr(typ, '__values__', None))


def remove_temp_options(options: Set[BaseOption]) -> Set[BaseOption]:
    return set([
      option for option in list(options)
      if not isinstance(option, BaseTempOption)
    ])