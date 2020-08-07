from py_type_extractor.test_fixtures.new_type import (
    name_by_id,
    SomeClassInNewType,
)
from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.NewType import NewTypeFound
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor


def test_newtype():
    type_extractor = TypeExtractor()
    type_extractor.add()(name_by_id)
    type_extractor.add()(SomeClassInNewType)
    cleaned_up = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
    }
    user_id_newtype = NewTypeFound(
        name='UserId',
        actual=int,
    )
    some_class = ClassFound(
        name='SomeClass',
        fields={
            'a': int,
        }
    )
    assert cleaned_up == {
        'UserId': user_id_newtype,
        'name_by_id': FunctionFound(
            name='name_by_id',
            params={
                'user_id': user_id_newtype,
            },
            return_type=str,
        ),
        'SomeClass': some_class,
        'SomeClassInNewType': NewTypeFound(
            name='SomeClassInNewType',
            actual=some_class,
        ),
    }
    print(1)
