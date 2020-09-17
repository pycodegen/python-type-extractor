import py_type_extractor.test_fixtures.classes_with_inheritance as t

from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

module_name = t.__name__


def test_classes_with_inheritance():
    type_extractor = TypeExtractor()

    type_extractor.add(None)(t.ChildClass)

    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    parent_class_a = ClassFound(
        module_name=module_name,
        name='ParentClassA',
        fields={
            'from_parent_a': int,
        },
    )
    parent_class_b = ClassFound(
        module_name=module_name,
        name='ParentClassB',
        fields={
            'from_parent_b': str,
        },
    )
    assert classes[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.ParentClassA.__qualname__,
               )
           ] == parent_class_a

    assert classes[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.ParentClassB.__qualname__,
               )
           ] == parent_class_b

    assert classes[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.ChildClass.__qualname__,
               )
           ] == ClassFound(
        module_name=module_name,
        name='ChildClass',
        fields={
            'b': str,
        },
        base_classes=[
            parent_class_a,
            parent_class_b,
        ],
    )
    hash_test(type_extractor)
