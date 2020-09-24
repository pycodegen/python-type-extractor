import py_type_extractor.test_fixtures.generic_classes  as t
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

module_name = t.__name__

def test_class_of_generic_origin():
    type_extractor = TypeExtractor()
    type_extractor.add()(t.SomeGenericClass)
    type_extractor.add()(t.SomeGenericClass)
    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    typevar_A = TypeVarFound(
        name='SomeTypeVarA',
        original=t.SomeTypeVarA,
    )
    typevar_B = TypeVarFound(
        name='SomeTypeVarB',
        original=t.SomeTypeVarB,
    )
    collected_types_key = type_extractor.to_collected_types_key(
        module_name=module_name,
        typ_name=t.SomeGenericClass.__qualname__,
    )
    assert classes == {
        collected_types_key: ClassFound(
            name='SomeGenericClass',
            fields={
                'a': typevar_A,
                'b': typevar_B,
                'some_int': int,
            },
            module_name=module_name,
            type_vars=[
                typevar_A, typevar_B,
            ]
        )
    }

    hash_test(type_extractor)