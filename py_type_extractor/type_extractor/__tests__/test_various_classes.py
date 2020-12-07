from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.nodes.DictFound import DictFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
import py_type_extractor.test_fixtures.various_classes as t

module_name = t.__name__


def test_various_classes():
    type_extractor = TypeExtractor()
    type_extractor.add(None)(t.SomeDataClass)
    type_extractor.add(None)(t.SomeNormalClass)
    type_extractor.add(None)(t.SomeNamedTuple)
    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    assert classes[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.SomeDataClass.__qualname__,
               )
           ] == ClassFound(
        module_name=module_name,
        name='SomeDataClass',
        fields={
            'sdcArg1': int,
            'sdcArg2': str,
        },
    )

    assert classes[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.SomeNormalClass.__qualname__,
               )
           ] == ClassFound(
        module_name=module_name,
        name='SomeNormalClass',
        fields={
            'checklist': DictFound(key=str, value=bool),
        },
    )

    assert classes[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.SomeNamedTuple.__qualname__,
               )
           ] == ClassFound(
        module_name=module_name,
        name='SomeNamedTuple',
        fields={
            'sntArg1': int,
            'sntArg2': float,
        },
    )
    assert len(classes) == 3

    functions = type_extractor.functions
    functions_list = functions.values()
    assert (functions_list.__len__() == 0)

    hash_test(type_extractor)


if __name__ == '__main__':
    test_various_classes()
