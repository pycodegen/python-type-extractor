from typing import Optional

from .BaseNodeType import BaseNodeType

# singleton like None
class INTERNAL___UnknownFound(BaseNodeType):  # type: ignore
    _instance: Optional['INTERNAL___UnknownFound'] = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(
                INTERNAL___UnknownFound, cls,
            ).__new__(cls)
        return cls._instance

# single-instance for efficiency...
unknown_found = INTERNAL___UnknownFound()
