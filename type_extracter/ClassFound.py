from collections import OrderedDict
from typing import NamedTuple

class ClassFound(NamedTuple):
    name: str
    filePath: str
    raw_fields: OrderedDict
    fields: OrderedDict
    doc: str