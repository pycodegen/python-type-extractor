from typing import Optional, Generic, TypeVar


TVar = TypeVar('TVar')

class ClassA:
    b: 'ClassB'


class ClassB:
    a: Optional[ClassA]


class ClassC:
    maybe_self: Optional['ClassC']


class ClassD(Generic[TVar]):
    maybe_self: Optional['ClassD[TVar]']
