from collections import OrderedDict

from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup
from py_type_extractor.type_extractor.type_extractor import TypeExtractor


def test_func_with_nested_arg_class():
    type_collector = TypeExtractor()

    class ChildClass:
        carg1: str

    class ParentClass:
        parg1: str
        parg2: ChildClass

    @type_collector.add(None)
    def func_with_nested_arg_class(a: ParentClass) -> ParentClass:
        return a

    cleanedup = traverse(type_collector.collected_types[ParentClass.__name__], cleanup)

    child_class = ClassFound(
        name='ChildClass',
        fields={
            'return': None,
            'carg1': str,
        },
        doc='',
        filePath='',
        raw_fields=OrderedDict(),
        class_raw=ChildClass,
    )
    parent_class = ClassFound(
        name="ParentClass",
        fields={
            'return': None,
            'parg1': str,
            'parg2': child_class,
        },
        doc='',
        filePath='',
        raw_fields=OrderedDict(),
        class_raw=ParentClass
    )
    parent_cleaned = traverse(parent_class, cleanup)
    assert(parent_cleaned == cleanedup)
