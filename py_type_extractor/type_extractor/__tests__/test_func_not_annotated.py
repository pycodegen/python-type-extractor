from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.UnknownFound import unknown_found
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
from py_type_extractor.test_fixtures.func_not_annotated import func_not_annotated


def test_func_not_annotated():
    type_collector = TypeExtractor()

    type_collector.add(None)(func_not_annotated)

    # assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.collected_types[func_not_annotated.__qualname__],
    )
    assert func_found_cleaned.return_type == unknown_found
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=func_not_annotated.__qualname__,
            params={
                'arg1': unknown_found,
            },
            return_type=unknown_found,
        ),
        cleanup,
    )
