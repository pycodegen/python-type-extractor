from dataclasses import dataclass

from py_type_extractor.test_fixtures.union_type_class import ClassWithUnionField
from py_type_extractor.type_extractor.nodes.BaseNodeType import BaseOption
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup
from py_type_extractor.type_extractor.type_extractor import TypeExtractor


@dataclass(frozen=True)
class SomeOption(BaseOption):
    some_var: int


def test_class_with_union_field():
    type_collector = TypeExtractor()

    type_collector.add(None)(ClassWithUnionField)
    type_collector.add({SomeOption(some_var=1)})(ClassWithUnionField)

    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_collector.collected_types.items()
        if isinstance(value, ClassFound)
    }
    assert classes == {
        'ClassWithUnionField': ClassFound(
            name='ClassWithUnionField',
            fields={
                'cwufField1': TypeOR(
                    a=str, b=int
                )
            },
            options={SomeOption(some_var=1)},
        )
    }
    functions = type_collector.functions
    assert functions == {}
