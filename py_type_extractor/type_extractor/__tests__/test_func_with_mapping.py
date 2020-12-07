from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse, hash_test
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.MappingFound import MappingFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
import py_type_extractor.test_fixtures.func_with_mapping as t

module_name = t.__name__


def test_func_with_mapping():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.func_with_mapping)

    func_found_cleaned = cleanup(
        type_collector.collected_types[
            type_collector.to_collected_types_key(
                module_name=module_name,
                typ_name=t.func_with_mapping.__qualname__,
            )
        ],
    )
    assert func_found_cleaned == traverse(
        FunctionFound(
            name=t.func_with_mapping.__qualname__,
            module_name=module_name,
            params={
              'input': MappingFound(key=str, value=int),
            },
            return_type=MappingFound(key=int, value=str),
        ),
        cleanup,
    )

    hash_test(type_collector)


if __name__ == '__main__':
    test_func_with_mapping()
