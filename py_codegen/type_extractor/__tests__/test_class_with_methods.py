from dataclasses import dataclass

from py_codegen.test_fixtures.class_with_methods import ClassWithMethod
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.TypeOR import TypeOR
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.type_extractor import TypeExtractor


@dataclass(frozen=True)
class SomeOption(BaseOption):
    some_var: int


def test_class_with_methods():
    type_collector = TypeExtractor()

    type_collector.add(None)(ClassWithMethod)

    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_collector.collected_types.items()
        if isinstance(value, ClassFound)
    }
    assert classes == {
        'ClassWithMethod': ClassFound(
            name='ClassWithMethod',
            fields={
                'temp': str,
            },
            custom_methods={

            }
        )
    }
    functions = type_collector.functions
    assert functions == {}
