from collections import OrderedDict

from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

module_name = __name__


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

    def to_collected_types_key(a):
        return type_collector.to_collected_types_key(
            module_name=module_name,
            typ_name= f'test_func_with_nested_arg_class.{a.__name__}'
        )
    cleanedup = traverse(
        type_collector.collected_types[to_collected_types_key(ParentClass)],
        cleanup,
    )

    child_class = ClassFound(
        name='test_func_with_nested_arg_class.ChildClass',
        module_name=module_name,
        fields={
            'carg1': str,
        },
        doc='',
        filePath='',
        raw_fields=OrderedDict(),
        class_raw=ChildClass,
    )
    parent_class = ClassFound(
        module_name=module_name,
        name="test_func_with_nested_arg_class.ParentClass",
        fields={
            'parg1': str,
            'parg2': child_class,
        },
        doc='',
        filePath='',
        raw_fields=OrderedDict(),
        class_raw=ParentClass
    )
    parent_cleaned = traverse(parent_class, cleanup)
    assert (parent_cleaned == cleanedup)

    hash_test(type_collector)


if __name__ == '__main__':
    test_func_with_nested_arg_class()
