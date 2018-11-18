from collections import OrderedDict
from dataclasses import dataclass

@dataclass
class ClassFound:
    # def __eq__(self, other):
    #     if not isinstance(other, ClassFound):
    #         return False
    #     if self.fields != other.fields:
    #         return False
    #     return True
    name: str
    filePath: str
    raw_fields: OrderedDict
    fields: OrderedDict
    doc: str