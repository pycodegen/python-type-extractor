from typing_extensions import (
    NewType,
)


UserId = NewType('UserId', int)


def name_by_id(user_id: UserId) -> str:
    return str(user_id)


class SomeClass:
    a: int


SomeClassInNewType = NewType('SomeClassInNewType', SomeClass)