from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.nodes.DictFound import DictFound
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.various_classes import (
    SomeDataClass,
    SomeNamedTuple,
    SomeNormalClass,
)


def test_various_classes():

    type_extractor = TypeExtractor()
    type_extractor.add_class(None)(SomeDataClass)
    type_extractor.add_class(None)(SomeNormalClass)
    type_extractor.add_class(None)(SomeNamedTuple)
    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.classes.items()
    }
    assert classes == {
        'SomeDataClass': ClassFound(
            name='SomeDataClass',
            fields={
                'sdcArg1': int,
                'sdcArg2': str,
            },
        ),
        'SomeNormalClass': ClassFound(
            name='SomeNormalClass',
            fields={
                'checklist': DictFound(key=str, value=bool),
            },
        ),
        'SomeNamedTuple': ClassFound(
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
