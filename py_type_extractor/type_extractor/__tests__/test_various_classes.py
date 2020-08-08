from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup
from py_type_extractor.type_extractor.nodes.DictFound import DictFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
from py_type_extractor.test_fixtures.various_classes import (
    SomeDataClass,
    SomeNamedTuple,
    SomeNormalClass,
)


def test_various_classes():

    type_extractor = TypeExtractor()
    type_extractor.add(None)(SomeDataClass)
    type_extractor.add(None)(SomeNormalClass)
    type_extractor.add(None)(SomeNamedTuple)
    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    assert classes == {
        'py_type_extractor.test_fixtures.various_classes.SomeDataClass': ClassFound(
            name='SomeDataClass',
            fields={
                'sdcArg1': int,
                'sdcArg2': str,
            },
        ),
        'py_type_extractor.test_fixtures.various_classes.SomeNormalClass': ClassFound(
            name='SomeNormalClass',
            fields={
                'checklist': DictFound(key=str, value=bool),
            },
        ),
        'py_type_extractor.test_fixtures.various_classes.SomeNamedTuple': ClassFound(
            name='SomeNamedTuple',
            fields={
                'sntArg1': int,
                'sntArg2': float,
            },
        )
    }
    functions = type_extractor.functions
    functions_list = functions.values()
    assert(functions_list.__len__() == 0)
