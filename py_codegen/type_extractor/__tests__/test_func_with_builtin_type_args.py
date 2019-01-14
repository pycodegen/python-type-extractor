from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.__tests__.utils import cleanup
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.func_with_builtin_type_args \
    import func_with_builtin_args


def test_func_with_builtin_type_args():
    type_collector = TypeExtractor()

    type_collector.add_function(None)(func_with_builtin_args)

    assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.functions['func_with_builtin_args'],
    )
    assert func_found_cleaned == cleanup(FunctionFound(
        name='func_with_builtin_args',
        params={
            'return': int,
            'a': int,
        },
        doc='',
        return_type=int,
        #
        func=None,
        filePath=None,
        raw_params=None,
    ))
