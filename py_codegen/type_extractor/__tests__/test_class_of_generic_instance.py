from py_codegen.test_fixtures.generic_classes import (
    some_func_with_generic_inst,
    SomeTypeVarA,
    SomeTypeVarB,
)
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_codegen.type_extractor.type_extractor import TypeExtractor


# noinspection PyPep8Naming
def test_class_of_generic_instance():
    type_extractor = TypeExtractor()
    type_extractor.add()(some_func_with_generic_inst)
    print(type_extractor)

    collected_types = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
    }
    some_typevar_A = TypeVarFound(
        name='SomeTypeVarA',
        original=SomeTypeVarA,
    )
    some_typevar_B = TypeVarFound(
        name='SomeTypeVarB',
        original=SomeTypeVarB,
    )
    some_generic_class = ClassFound(
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
    some_class = ClassFound(
        name='SomeClass',
        fields={
            'some_property': int,
        }
    )
    assert collected_types['SomeGenericClass'] == some_generic_class

    assert collected_types['SomeClass'] == some_class

    assert collected_types['some_func_with_generic_inst'] == FunctionFound(
        name='some_func_with_generic_inst',
        params={
            'input': FixedGenericFound(
                type_vars=[float, some_class],
                origin=some_generic_class,
            )
        },
        return_type=str,
    )

