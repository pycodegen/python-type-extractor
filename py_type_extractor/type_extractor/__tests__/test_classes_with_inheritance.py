from py_type_extractor.test_fixtures.classes_with_inheritance import ChildClass

from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup
from py_type_extractor.type_extractor.type_extractor import TypeExtractor


def test_classes_with_inheritance():
    type_extractor = TypeExtractor()

    type_extractor.add(None)(ChildClass)

    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    parent_class_a = ClassFound(
        name='ParentClassA',
        fields={
            'from_parent_a': int,
        },
    )
    parent_class_b = ClassFound(
        name='ParentClassB',
        fields={
            'from_parent_b': str,
        },
    )
    assert classes == {
        'py_type_extractor.test_fixtures.classes_with_inheritance.ParentClassA': parent_class_a,
        'py_type_extractor.test_fixtures.classes_with_inheritance.ParentClassB': parent_class_b,
        'py_type_extractor.test_fixtures.classes_with_inheritance.ChildClass': ClassFound(
            name='ChildClass',
            fields={
                'b': str,
            },
            base_classes=[
                parent_class_a,
                parent_class_b,
            ],
        )
    }
    print(type_extractor)
