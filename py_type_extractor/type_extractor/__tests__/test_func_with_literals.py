from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse, hash_test
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.LiteralFound import LiteralFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

import py_type_extractor.test_fixtures.func_with_literals as t

module_name = t.__name__


def test_func_with_list():
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
                'input1': TypeOR(
                    a=LiteralFound('a'),
                    b=TypeOR(
                        a=LiteralFound(1),
                        b=TypeOR(
                            a=TypeOR(
                                a=LiteralFound(2),
                                b=LiteralFound(3),
                            ),
                            b=TypeOR(
                                a=LiteralFound(True),
                                b=LiteralFound(3),
                            ),
                        ),
                    ),
                ),
                'input2': TypeOR(
                    a=LiteralFound(1),
                    b=LiteralFound(None),
                ),
            },
            return_type=TypeOR(
                a=LiteralFound(True),
                b=TypeOR(
                    a=LiteralFound(5),
                    b=LiteralFound(3),
                ),
            )
        ),
        cleanup,
    )
    assert func_found_cleaned == expected_func_found_cleaned

    hash_test(type_collector)