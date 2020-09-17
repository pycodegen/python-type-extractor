import py_type_extractor.test_fixtures.new_type as t

from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.NewType import NewTypeFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

module_name = t.__name__


def test_newtype():
    type_extractor = TypeExtractor()
    type_extractor.add()(t.name_by_id)
    type_extractor.add()(t.SomeClassInNewType)
    cleaned_up = {
        key: traverse(value, cleanup)
        for (key, value) in type_extractor.collected_types.items()
    }
    user_id_newtype = NewTypeFound(
        name=t.UserId.__name__,
        actual=int,
        original_ref=t.UserId,
    )
    some_class = ClassFound(
        module_name=module_name,
        name='SomeClass',
        fields={
            'a': int,
        }
    )
    assert cleaned_up[t.UserId.__name__] == user_id_newtype

    assert cleaned_up[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.name_by_id.__qualname__,
               )
           ] == FunctionFound(
        module_name=module_name,
        name='name_by_id',
        params={
            'user_id': user_id_newtype,
        },
        return_type=str,
    )

    assert cleaned_up[
               type_extractor.to_collected_types_key(
                   module_name=module_name,
                   typ_name=t.SomeClass.__qualname__,
               )
           ] == some_class

    assert cleaned_up[t.SomeClassInNewType.__name__] == NewTypeFound(
        name='SomeClassInNewType',
        actual=some_class,
        original_ref=t.SomeClassInNewType,
    )

    hash_test(type_extractor)
