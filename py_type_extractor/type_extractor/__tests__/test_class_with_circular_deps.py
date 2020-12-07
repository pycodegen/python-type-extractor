from py_type_extractor.type_extractor.__tests__.utils import hash_test, traverse, cleanup
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
import py_type_extractor.test_fixtures.class_with_circular_deps as t


def test_class_with_circular_deps():
    # TODO: make Lazy?
    #  hashing by:
    type_extractor = TypeExtractor()
    type_extractor.add()(t.ClassA)
    type_extractor.add()(t.ClassC)
    # type_extractor.add()(t.ClassD)

    collected_types = {
        key: traverse(value, cleanup)
        for (key, value)
        in type_extractor.collected_types.items()
    }

    hash_test(type_extractor)


if __name__ == '__main__':
    test_class_with_circular_deps()