from py_codegen.type_extractor.__tests__.utils import cleanup, traverse
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.ListFound import ListFound
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.func_with_list import func_with_list


def test_func_with_list():
    type_collector = TypeExtractor()

    type_collector.add_function(None)(func_with_list)

    # assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.functions[func_with_list.__qualname__],
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=func_with_list.__qualname__,
            params={
                'input': ListFound(str),
            },
            return_type=ListFound(str),
        ),
        cleanup,
    )
