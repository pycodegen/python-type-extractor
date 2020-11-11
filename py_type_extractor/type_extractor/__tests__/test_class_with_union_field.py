from dataclasses import dataclass

import py_type_extractor.test_fixtures.union_type_class as t
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.type_extractor import TypeExtractor


@dataclass(frozen=True)
class SomeOption(BaseOption):
    some_var: int

module_name = t.__name__

def test_class_with_union_field():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.ClassWithUnionField)
    type_collector.add({SomeOption(some_var=1)})(t.ClassWithUnionField)

    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_collector.collected_types.items()
        if isinstance(value, ClassFound)
    }
    key = type_collector.to_collected_types_key(
        module_name,
        t.ClassWithUnionField.__qualname__
    )
    to_compare = {
        key: ClassFound(
            name='ClassWithUnionField',
            fields={
                'cwufField1': TypeOR(
                    a=str, b=int
                )
            },
            module_name=module_name,
            options={SomeOption(some_var=1)},
        )
    }
    assert to_compare == classes

    hash_test(type_collector)