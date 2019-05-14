from py_codegen.type_extractor.__tests__.utils import cleanup, traverse
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.TupleFound import TupleFound
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.func_with_tuple import func_with_tuple


def test_func_with_tuple():
    type_collector = TypeExtractor()

    type_collector.add(None)(func_with_tuple)

    # assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.collected_types[func_with_tuple.__qualname__],
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=func_with_tuple.__qualname__,
            params={
              'input': TupleFound([str, int]),
            },
            return_type=TupleFound([int, str]),
        ),
        cleanup,
    )
