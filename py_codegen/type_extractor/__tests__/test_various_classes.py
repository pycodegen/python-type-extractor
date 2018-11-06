from py_codegen.type_extractor import TypeExtractor
from py_codegen.test_fixtures.various_classes import SomeDataClass, SomeNamedTuple, SomeNormalClass

def test_various_classes():

    type_extractor = TypeExtractor()
    type_extractor.add_class(None)(SomeDataClass)
    type_extractor.add_class(None)(SomeNormalClass)
    type_extractor.add_class(None)(SomeNamedTuple)
    classes = type_extractor.classes
    classes_list = classes.values()
    assert(classes_list.__len__() == 3)

    functions = type_extractor.functions
    functions_list = functions.values()
    assert(functions_list.__len__() == 0)
