from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup
from py_type_extractor.type_extractor.__tests__.utils.flags.KeepClassMethods import (
    keep_class_methods,
)
from py_type_extractor.type_extractor.__tests__.utils.hash_test import hash_test
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.nodes.__flags import FromMethod
from py_type_extractor.type_extractor.type_extractor import TypeExtractor
import py_type_extractor.test_fixtures.class_with_methods as t

module_name = t.__name__

def test_class_with_method():
    type_extractor = TypeExtractor()
    type_extractor.add()(t.ClassWithMethod)

    classes = {
        key: traverse(value, cleanup, None, { keep_class_methods })
        for (key, value) in type_extractor.collected_types.items()
        if isinstance(value, ClassFound)
    }

    class_type_key = type_extractor.to_collected_types_key(
        module_name=module_name,
        typ_name=t.ClassWithMethod.__qualname__,
    )
    some_method = FunctionFound(
        name='some_method',
        module_name=module_name,
        params={
            'arg': int,
        },
        return_type=int,
    )
    class_found = ClassFound(
        methods={
            'some_method': some_method,
        },
        fields={},
        module_name=module_name,
        name=t.ClassWithMethod.__qualname__,
    )
    some_method.options = {
        FromMethod(
            method_name='some_method',
        )
    }
    assert classes[class_type_key] == class_found
    print(type_extractor)

    hash_test(type_extractor)