from py_codegen.type_extractor.__tests__.utils import cleanup, traverse
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.MappingFound import MappingFound
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.func_with_mapping import func_with_mapping


def test_func_with_tuple():
    type_collector = TypeExtractor()

    type_collector.add(None)(func_with_mapping)

    func_found_cleaned = cleanup(
        type_collector.collected_types[func_with_mapping.__qualname__],
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=func_with_mapping.__qualname__,
            params={
              'input': MappingFound(key=str, value=int),
            },
            return_type=MappingFound(key=int, value=str),
        ),
        cleanup,
    )
