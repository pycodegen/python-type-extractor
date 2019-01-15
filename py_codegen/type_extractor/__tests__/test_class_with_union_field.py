from py_codegen.test_fixtures.union_type_class import ClassWithUnionField
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.TypeOR import TypeOR
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_class_with_union_field():
    type_collector = TypeExtractor()

    type_collector.add_class(None)(ClassWithUnionField)

    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_collector.classes.items()
    }
    assert classes == {
        'ClassWithUnionField': ClassFound(
            name='ClassWithUnionField',
            fields={
                'cwufField1': TypeOR(
                    a=str, b=int
                )
            },
        )
    }
    functions = type_collector.functions
    assert functions == {}
