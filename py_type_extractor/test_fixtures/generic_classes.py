from typing import TypeVar, Generic

SomeTypeVarA = TypeVar('SomeTypeVarA')

SomeTypeVarB = TypeVar('SomeTypeVarB', int, str)


class SomeGenericClass(Generic[SomeTypeVarA, SomeTypeVarB]):
    a: SomeTypeVarA
    b: SomeTypeVarB
    some_int: int


SomeTypeVarC = TypeVar('SomeTypeVarA')


class SomeGenericClassWithInst(Generic[SomeTypeVarC]):
    c: SomeTypeVarC

    def __init__(self, c: SomeTypeVarC):
        self.c = c


some_generic_class_inst = SomeGenericClassWithInst[int](3)


class SomeClass:
    some_property: int


def some_func_with_generic_inst(
    input: SomeGenericClass[float, SomeClass]
) -> str:
    return 'hello'
