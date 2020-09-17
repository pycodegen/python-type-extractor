import py_type_extractor.test_fixtures.func_with_arg_class as t
from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse, hash_test
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

module_name = t.__name__

def test_func_with_arg_class():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.func_with_arg_class)
    collected_types_key = type_collector.to_collected_types_key(
        module_name=module_name,
        typ_name='func_with_arg_class',
    )
    func_found_cleaned = traverse(
        type_collector.collected_types[collected_types_key],
        cleanup,
    )
    arg_class_found = ClassFound(
        name='ArgClass',
        module_name=module_name,
        fields={
            'arg1': str,
            'arg2': int,
        },
    )
    assert func_found_cleaned == cleanup(
        FunctionFound(
            name='func_with_arg_class',
            module_name=module_name,
            params={
                'a': arg_class_found,
            },
            doc='',
            return_type=arg_class_found,
            #
            func=None,
        )
    )

    hash_test(type_collector)
