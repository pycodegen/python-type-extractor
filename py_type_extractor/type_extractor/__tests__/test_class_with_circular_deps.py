from py_type_extractor.type_extractor.__tests__.utils import hash_test
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
from py_type_extractor.test_fixtures.class_with_circular_deps import (
    ClassA,
)

def test_class_of_generic_origin():
    # TODO: make Lazy?
    #  hashing by:
    type_extractor = TypeExtractor()
    type_extractor.add()(ClassA)
    print(type_extractor)

    #   fixme: circular-dep hash
    hash_test(type_extractor)