from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse, hash_test
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.LiteralFound import LiteralFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

import py_type_extractor.test_fixtures.func_with_literals as t

module_name = t.__name__


def test_func_with_literals():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.func_with_literals)

    original_func_found = type_collector.collected_types[
        type_collector.to_collected_types_key(
            module_name=module_name,
            typ_name=t.func_with_literals.__qualname__,
        )
    ]
    func_found_cleaned = cleanup(original_func_found)
    expected_func_found_cleaned = traverse(
        FunctionFound(
            name=t.func_with_literals.__qualname__,
            module_name=module_name,
            params={
                'input1': LiteralFound({
                    'a', 1, 2, 3, True,
                }),
                'input2': LiteralFound({
                    1, None,
                }),
            },
            return_type=LiteralFound({
                True, 3, 5,
            }),
        ),
        cleanup,
    )
    assert func_found_cleaned == expected_func_found_cleaned

    hash_test(type_collector)


if __name__ == '__main__':
    test_func_with_literals()