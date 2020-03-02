from py_codegen.test_fixtures.class_with_methods import ClassWithMethods
from py_codegen.type_extractor.__tests__.utils import cleanup, traverse
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound
from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_class_with_methods():
    type_extractor = TypeExtractor()
    type_extractor.add()(ClassWithMethods)
    print(type_extractor)