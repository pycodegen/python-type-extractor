from dataclasses import dataclass
from typing import NamedTuple, Dict


@dataclass
class SomeDataClass:
    sdcArg1: int
    sdcArg2: str


class SomeNamedTuple(NamedTuple):
    sntArg1: int
    sntArg2: float


class SomeNormalClass:
    checklist: Dict[str, bool]
