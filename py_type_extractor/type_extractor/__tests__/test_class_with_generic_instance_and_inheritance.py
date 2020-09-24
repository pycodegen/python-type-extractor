import py_type_extractor.test_fixtures.generic_classes_extended as t
import py_type_extractor.test_fixtures.generic_classes as t2

from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
from py_type_extractor.type_extractor.utils.generics import flatten_generics_inheritance_to

module_name = t.__name__
module2_name = t2.__name__

# noinspection PyPep8Naming
def test_class_with_generic_instance_and_inheritance():
    type_extractor = TypeExtractor()
    type_extractor.add()(t.SomeGenericInheritanceClass)
    type_extractor.add()(t.SomeGenericInheritanceClass)
    type_extractor.add()(t.SomeGenericInheritanceClassWithTypevarsSet)
    type_extractor.add()(t.SomeGenericInheritanceClassWithTypevarsSet)

    collected_types = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
    }

    not_generic_class = ClassFound(
        module_name=module_name,
        name=t.NotGenericClass.__qualname__,
        fields={
            'a': int,
        }
    )


    assert collected_types[
        type_extractor.to_collected_types_key(
            module_name=module_name,
            typ_name=t.NotGenericClass.__qualname__,
        )
    ] == not_generic_class

    some_typevar_A = TypeVarFound(
        name='SomeTypeVarA',
        original=t2.SomeTypeVarA,
    )
    some_typevar_B = TypeVarFound(
        name='SomeTypeVarB',
        original=t2.SomeTypeVarB,
    )

    some_generic_class = ClassFound(
        module_name=module2_name,
        name='SomeGenericClass',
        fields={
            'a': some_typevar_A,
            'b': some_typevar_B,
            'some_int': int,
        },
        type_vars=[
            some_typevar_A, some_typevar_B,
        ],
    )

    assert collected_types[
        type_extractor.to_collected_types_key(
            module_name=module2_name,
            typ_name=t2.SomeGenericClass.__qualname__,
        )
    ] == some_generic_class

    some_generic_class = ClassFound(
        module_name=module2_name,
        name='SomeGenericClass',
        fields={
            'a': some_typevar_A,
            'b': some_typevar_B,
            'some_int': int,
        },
        type_vars=[
            some_typevar_A, some_typevar_B,
        ],
    )

    extended_tvar1 = TypeVarFound(
        name='ExtendedTVar1',
        original=t.ExtendedTVar1,
    )
    extended_tvar2 = TypeVarFound(
        name='ExtendedTVar2',
        original=t.ExtendedTVar2,
    )
    extended_tvar2 = TypeVarFound(
        name='ExtendedTVar2',
        original=t.ExtendedTVar2,
    )
    some_generic_inheritance_class = ClassFound(
        module_name=module_name,
        name=t.SomeGenericInheritanceClass.__qualname__,
        type_vars=[extended_tvar1, extended_tvar2, some_typevar_B],
        fields={
            'a': int,
        },
        base_classes=[
            not_generic_class,
            FixedGenericFound(
                origin=some_generic_class,
                type_vars=[extended_tvar1, some_typevar_B],
            )
        ]
    )

    assert collected_types[
        type_extractor.to_collected_types_key(
            module_name=module_name,
            typ_name=t.SomeGenericInheritanceClass.__qualname__,
        )
    ] == some_generic_inheritance_class

    extended_tvarA = TypeVarFound(
        name='ExtendedTVarA',
        original=t.ExtendedTVarA,
    )

    some_generic_inheritance_class_with_typevarsSet = ClassFound(
        module_name=module_name,
        name=t.SomeGenericInheritanceClassWithTypevarsSet.__qualname__,
        type_vars=[extended_tvarA],
        fields={
            'a': int,
        },
        base_classes=[
            FixedGenericFound(
                origin=some_generic_inheritance_class,
                type_vars=[float, extended_tvarA, str],
            )
        ],
    )

    assert collected_types[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.SomeGenericInheritanceClassWithTypevarsSet.__qualname__,
               )
           ] == some_generic_inheritance_class_with_typevarsSet

    flattened = flatten_generics_inheritance_to(
        from_typ=some_generic_inheritance_class_with_typevarsSet,
        to_typ=some_generic_class,
    )
    assert flattened == [
        FixedGenericFound(
            origin=some_generic_class,
            type_vars=[float, str]
        )
    ]
