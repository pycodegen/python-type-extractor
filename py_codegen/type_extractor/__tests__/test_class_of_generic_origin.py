from py_codegen.test_fixtures.generic_classes import (
    SomeGenericClass,
    SomeTypeVarA,
    SomeTypeVarB,
)
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_class_of_generic_origin():
    type_extractor = TypeExtractor()
    type_extractor.add()(SomeGenericClass)
    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    typevar_A = TypeVarFound(
        name='SomeTypeVarA',
        original=SomeTypeVarA,
    )
    typevar_B = TypeVarFound(
        name='SomeTypeVarB',
        original=SomeTypeVarB,
    )
    assert classes == {
        'SomeGenericClass': ClassFound(
            name='SomeGenericClass',
            fields={
                'a': typevar_A,
                'b': typevar_B,
                'some_int': int,
            },
            type_vars=[
                typevar_A, typevar_B,
            ]
        )
    }
