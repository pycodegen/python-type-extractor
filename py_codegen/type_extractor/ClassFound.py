from collections import OrderedDict
from dataclasses import dataclass
from typing import Optional


@dataclass(
    order=True,
)
class ClassFound:
    name: str
    filePath: str
    raw_fields: OrderedDict
    fields: OrderedDict
    doc: str
    class_raw: Optional[type] = None

