import py_type_extractor.test_fixtures.generic_classes as t
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

module_name = t.__name__

# noinspection PyPep8Naming
def test_func_with_generic_instance():
    type_extractor = TypeExtractor()
    type_extractor.add()(t.some_func_with_generic_inst)
    print(type_extractor)

    collected_types = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
    }
    some_typevar_A = TypeVarFound(
        name='SomeTypeVarA',
        original=t.SomeTypeVarA,
    )
    some_typevar_B = TypeVarFound(
        name='SomeTypeVarB',
        original=t.SomeTypeVarB,
    )
    some_generic_class = ClassFound(
        module_name=module_name,
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
        module_name=module_name,
        name='SomeClass',
        fields={
            'some_property': int,
        }
    )
    assert collected_types[
        type_extractor.to_collected_types_key(
            module_name=module_name,
            typ_name=t.SomeGenericClass.__qualname__,
        )
   ] == some_generic_class

    assert collected_types[
        type_extractor.to_collected_types_key(
            module_name=module_name,
            typ_name=t.SomeClass.__qualname__,
        )
   ] == some_class

    assert collected_types[
        type_extractor.to_collected_types_key(
            module_name=module_name,
            typ_name=t.some_func_with_generic_inst.__qualname__,
        )
    ] == FunctionFound(
        name='some_func_with_generic_inst',
        module_name=module_name,
        params={
            'input': FixedGenericFound(
                type_vars=[float, some_class],
                origin=some_generic_class,
            )
        },
        return_type=str,
    )

    hash_test(type_extractor)

