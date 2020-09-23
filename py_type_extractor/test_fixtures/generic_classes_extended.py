import py_type_extractor.test_fixtures.generic_classes as t
from py_type_extractor.test_fixtures.generic_classes import (
    SomeTypeVarB
)

from typing import TypeVar, Generic

ExtendedTVar1 = TypeVar('ExtendedTVar1')
ExtendedTVar2 = TypeVar('ExtendedTVar2')
ExtendedTVar3 = TypeVar('ExtendedTVar3')

ExtendedTVarA = TypeVar('ExtendedTVarA')

class NotGenericClass:
    a: int

class SomeGenericInheritanceClass(
    NotGenericClass,
    t.SomeGenericClass[ExtendedTVar1, t.SomeTypeVarB],
    Generic[ExtendedTVar1, ExtendedTVar2, SomeTypeVarB]
):
    pass

    '''
    typing_inspect.get_parameters(t.SomeGenericClass) --> (~SomeTypeVarA, ~SomeTypeVarB)


    '''

class SomeGenericInheritanceClassWithTypevarsSet(
    SomeGenericInheritanceClass[float, ExtendedTVarA, str],
    Generic[ExtendedTVarA]
):
    pass