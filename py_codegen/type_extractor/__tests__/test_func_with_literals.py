from py_codegen.type_extractor.__tests__.utils import cleanup, traverse
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.nodes.LiteralFound import LiteralFound
from py_codegen.type_extractor.nodes.TypeOR import TypeOR
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.func_with_literals import func_with_literals


def test_func_with_list():
    type_collector = TypeExtractor()

    type_collector.add(None)(func_with_literals)

    original_func_found = type_collector.collected_types[func_with_literals.__qualname__]
    func_found_cleaned = cleanup(original_func_found)
    expected_func_found_cleaned = traverse(
        FunctionFound(
            name=func_with_literals.__qualname__,
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
