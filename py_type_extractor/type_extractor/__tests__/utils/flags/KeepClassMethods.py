from dataclasses import dataclass

from py_type_extractor.type_extractor.__tests__.utils.flags.__base__ import BaseUtilFlag


@dataclass(frozen=True)
class KeepClassMethods(BaseUtilFlag):
    pass


keep_class_methods = KeepClassMethods()
