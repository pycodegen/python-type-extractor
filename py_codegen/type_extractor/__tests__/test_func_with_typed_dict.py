from py_codegen.test_fixtures.func_with_typed_dict import func_with_typed_dict
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.TypedDictFound import TypedDictFound
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.type_extractor.__tests__.utils import cleanup, traverse


def test_func_with_typed_dict():
    type_collector = TypeExtractor()

    type_collector.add_function(None)(func_with_typed_dict)
    func = type_collector.functions['func_with_typed_dict']
    cleaned_func = traverse(func, cleanup)

    to_compare_func = traverse(
        FunctionFound(
            name=func_with_typed_dict.__qualname__,
            params={
                'input': TypedDictFound(
                    name='NestedTypedDict',
                    annotations={
                        'child': TypedDictFound(
                            name='SimpleTypedDict1',
                            annotations={
                                'a': str,
                            },
                        )
                    },
                )
            },
            return_type=TypedDictFound(
                annotations={
                    'b': int,
                    's': ClassFound(
                        name='SomeClass',
                        fields={
                            'a': int,
                        }
                    )
                },
                name='OutputType'
            )
        ),
        cleanup,
    )
    assert cleaned_func == to_compare_func
