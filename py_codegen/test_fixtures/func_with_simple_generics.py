from typing import TypeVar, Generic

SomeTypeVarA = TypeVar('SomeTypeVarA')

SomeTypeVarB = TypeVar('SomeTypeVarB', int, str)


class SomeGenericClass(Generic[SomeTypeVarA, SomeTypeVarB]):
    a: SomeTypeVarA
    b: SomeTypeVarB


def some_func_with_generics(some_generic_instance: SomeGenericClass[float, int]) -> None:
    print(some_generic_instance)
    pass


print(some_func_with_generics)

