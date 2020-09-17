from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse, hash_test
from py_type_extractor.type_extractor.nodes.DictFound import DictFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.UnknownFound import unknown_found
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

import py_type_extractor.test_fixtures.func_with_dict as t

module_name=t.__name__

def test_func_with_dict():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.func_with_dict)

    func_found_cleaned = traverse(
        # type_collector.collected_types[func_with_dict.__qualname__],
        type_collector.collected_types[
            type_collector.to_collected_types_key(
                module_name=module_name,
                typ_name=t.func_with_dict.__qualname__,
            )
        ],
        cleanup,
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=t.func_with_dict.__qualname__,
            module_name=module_name,
            params={
                'input': DictFound(key=str, value=int),
            },
            return_type=DictFound(key=unknown_found, value=unknown_found),
        ),
        cleanup,
    )

    hash_test(type_collector)