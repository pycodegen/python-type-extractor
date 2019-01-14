from collections import OrderedDict

from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_func_with_nested_arg_class():
    type_collector = TypeExtractor()

    class ChildClass:
        carg1: str

    class ParentClass:
        parg1: str
        parg2: ChildClass

    @type_collector.add_function(None)
    def func_with_nested_arg_class(a: ParentClass) -> ParentClass:
        return a

    classes = type_collector.classes
    classes_list = classes.values()
    functions = type_collector.functions
    functions_list = functions.values()

    cleanedup = traverse(classes[ParentClass.__name__], cleanup)

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
    assert (classes_list.__len__() == 2)
    assert (functions_list.__len__() == 1)
