from typing import Dict, cast
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

import py_type_extractor.test_fixtures.pydantic_classes as t

module_name = t.__name__

def test_pydantic_classes():
    type_extractor = TypeExtractor()
    type_extractor.add(None)(t.SomePydanticModelClass)
    type_extractor.add(None)(t.SomePydanticDataClass)

    print(type_extractor)
    classes = cast(
        Dict[str, ClassFound],
        {
            key: traverse(value, cleanup)
            for (key, value) in type_extractor.collected_types.items()
            if isinstance(value, ClassFound)
        },
    )
    assert classes[
        type_extractor.to_collected_types_key(
            module_name=module_name,
            typ_name=t.SomePydanticDataClass.__qualname__,  # type: ignore
        )
    ] == ClassFound(
        name='SomePydanticDataClass',
        module_name=module_name,
        fields={
            'a': int,
            'b': str,
        },
    )

    assert classes[
        type_extractor.to_collected_types_key(
            module_name=module_name,
            typ_name=t.SomePydanticModelClass.__qualname__,
        )
    ] == ClassFound(
        name='SomePydanticModelClass',
        module_name=module_name,
        fields={
            'c': int,
            'something': float,
        },
        base_classes=[
            classes[
                type_extractor.to_collected_types_key(
                    module_name='pydantic.main',
                    typ_name='BaseModel',
                )
            ]
        ]
    )

    hash_test(type_extractor)


if __name__ == '__main__':
    test_pydantic_classes()
