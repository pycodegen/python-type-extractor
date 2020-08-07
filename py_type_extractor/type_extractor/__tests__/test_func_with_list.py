from dataclasses import dataclass

from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseOption
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.ListFound import ListFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
from py_type_extractor.test_fixtures.func_with_list import func_with_list


@dataclass(frozen=True)
class SomeOption(BaseOption):
    some_var: int


def test_func_with_list():
    type_collector = TypeExtractor()

    type_collector.add(
        options={SomeOption(some_var=3)}
    )(func_with_list)

    type_collector.add(
        options={SomeOption(some_var=5)}
    )(func_with_list)

    # assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.collected_types[func_with_list.__qualname__],
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=func_with_list.__qualname__,
            params={
                'input': ListFound(str),
            },
            return_type=ListFound(str),
            options={SomeOption(some_var=3), SomeOption(some_var=5)},
        ),
        cleanup,
    )
