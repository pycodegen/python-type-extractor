from py_codegen.type_extractor.__tests__.utils import cleanup, traverse
from py_codegen.type_extractor.nodes.DictFound import DictFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.func_with_dict import func_with_dict


def test_func_with_dict():
    type_collector = TypeExtractor()

    type_collector.add(None)(func_with_dict)

    func_found_cleaned = traverse(
        type_collector.collected_types[func_with_dict.__qualname__],
        cleanup,
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=func_with_dict.__qualname__,
            params={
                'input': DictFound(key=str, value=int),
            },
            return_type=DictFound(key=str, value=int),
        ),
        cleanup,
    )
