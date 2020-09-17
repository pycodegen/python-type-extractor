from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse, hash_test
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.UnknownFound import unknown_found
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
import py_type_extractor.test_fixtures.func_not_annotated as t

module_name = t.__name__

def test_func_not_annotated():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.func_not_annotated)

    # assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.collected_types[
            type_collector.to_collected_types_key(
                module_name=module_name,
                typ_name=t.func_not_annotated.__qualname__,
            )
        ]
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=t.func_not_annotated.__qualname__,
            module_name=module_name,
            params={
                'arg1': unknown_found,
            },
            return_type=unknown_found,
        ),
        cleanup,
    )

    hash_test(type_collector)