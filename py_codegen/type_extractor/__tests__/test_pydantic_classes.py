from pydantic import BaseModel

from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.nodes.DictFound import DictFound
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.pydantic_classes import (
    SomePydanticDataClass,
    SomePydanticModelClass,
)


def test_various_classes():
    type_extractor = TypeExtractor()
    type_extractor.add(None)(SomePydanticModelClass)
    type_extractor.add(None)(SomePydanticDataClass)

    print(type_extractor)
    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    assert classes['SomePydanticDataClass'] == ClassFound(
        name='SomePydanticDataClass',
        fields={
            'a': int,
            'b': str,
        },
    )

    assert classes['SomePydanticModelClass'] == ClassFound(
        name='SomePydanticModelClass',
        fields={
            'c': int,
            'something': float,
        },
        base_classes=[classes['BaseModel']],
    )
