import py_type_extractor.test_fixtures.func_with_typed_dict as t
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse, hash_test

module_name = t.__name__

def test_func_with_typed_dict():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.func_with_typed_dict)

    collected_types_key = type_collector.to_collected_types_key(
        module_name=module_name,
        typ_name='func_with_typed_dict'
    )
    func = type_collector.collected_types[collected_types_key]
    cleaned_func = traverse(func, cleanup)

    to_compare_func = traverse(
        FunctionFound(
            name=t.func_with_typed_dict.__qualname__,
            module_name=module_name,
            params={
                'input': TypedDictFound(
                    name='NestedTypedDict',
                    module_name=module_name,
                    annotations={
                        'child': TypedDictFound(
                            name='SimpleTypedDict1',
                            annotations={
                                'a': str,
                            },
                            module_name=module_name,
                        )
                    },
                )
            },
            return_type=TypedDictFound(
                module_name=module_name,
                annotations={
                    'b': int,
                    'some thing': str,
                    's': ClassFound(
                        name='SomeClass',
                        fields={
                            'a': int,
                        },
                        module_name=module_name,
                    )
                },
                name='OutputType'
            )
        ),
        cleanup,
    )
    assert cleaned_func == to_compare_func

    hash_test(type_collector)


if __name__ == '__main__':
    test_func_with_typed_dict()
