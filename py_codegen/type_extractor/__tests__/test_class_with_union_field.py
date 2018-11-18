from py_codegen.test_fixtures.union_type_class import ClassWithUnionField
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_class_with_union_field():
    type_collector = TypeExtractor()

    type_collector.add_class(None)(ClassWithUnionField)

    classes = type_collector.classes
    classes_list = classes.values()
    functions = type_collector.functions
    functions_list = functions.values()

    # traverse(classes_list[0], lambda node: print(node))

