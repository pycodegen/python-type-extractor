import py_type_extractor.test_fixtures.enum_class as t

from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.nodes.EnumFound import EnumFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

module_name = t.__name__


def test_enum_class():
    type_extractor = TypeExtractor()

    type_extractor.add(None)(t.SomeEnumClass)

    enums = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, EnumFound)
    }
    assert enums[type_extractor.to_collected_types_key(
        module_name=module_name,
        typ_name=t.SomeEnumClass.__qualname__,
    )] == EnumFound(
        members={
            'AAAAA': 1,
            'BBBBB': 2,
        },
        doc='An enumeration.',
        module_name=module_name,
        name=t.SomeEnumClass.__qualname__,
    )
    hash_test(type_extractor)


if __name__ == '__main__':
    test_enum_class()
