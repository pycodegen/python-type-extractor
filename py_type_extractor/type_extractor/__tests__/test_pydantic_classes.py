from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
from py_type_extractor.test_fixtures.pydantic_classes import (
    SomePydanticDataClass,
    SomePydanticModelClass,
)


def test_pydantic_classes():
    type_extractor = TypeExtractor()
    type_extractor.add(None)(SomePydanticModelClass)
    type_extractor.add(None)(SomePydanticDataClass)

    print(type_extractor)
    classes = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }
    assert classes[
        'py_type_extractor.test_fixtures.pydantic_classes.SomePydanticDataClass'
    ] == ClassFound(
        name='SomePydanticDataClass',
        fields={
            'a': int,
            'b': str,
        },
    )

    assert classes[
        'py_type_extractor.test_fixtures.pydantic_classes.SomePydanticModelClass'
    ] == ClassFound(
        name='SomePydanticModelClass',
        fields={
            'c': int,
            'something': float,
        },
        base_classes=[classes['pydantic.main.BaseModel']],
    )
