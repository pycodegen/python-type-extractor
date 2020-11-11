from dataclasses import dataclass

from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.ListFound import ListFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
import py_type_extractor.test_fixtures.func_with_list as t


module_name = t.__name__


@dataclass(frozen=True)
class SomeOption(BaseOption):
    some_var: int


def test_func_with_list():
    type_collector = TypeExtractor()

    type_collector.add(
        options={SomeOption(some_var=3)}
    )(t.func_with_list)

    type_collector.add(
        options={SomeOption(some_var=5)}
    )(t.func_with_list)

    # assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.collected_types[
            type_collector
                .to_collected_types_key(
                    module_name=module_name,
                    typ_name=t.func_with_list.__qualname__,
                )
        ],
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=t.func_with_list.__qualname__,
            module_name=module_name,
            params={
                'input': ListFound(str),
            },
            return_type=ListFound(str),
            options={SomeOption(some_var=3), SomeOption(some_var=5)},
        ),
        cleanup,
    )

    hash(func_found_cleaned)
