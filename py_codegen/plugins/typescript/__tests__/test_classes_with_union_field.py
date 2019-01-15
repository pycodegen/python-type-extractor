from py_codegen.plugins.typescript.Converter import TypescriptConverter

from py_codegen.test_fixtures.union_type_class import ClassWithUnionField
from py_codegen.test_fixtures.func_with_dict import func_with_dict
from py_codegen.test_fixtures.func_with_list import func_with_list
from py_codegen.test_fixtures.func_with_typed_dict import func_with_typed_dict

from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_typescript_converter_classes_with_union_field():
    type_collector = TypeExtractor()
    type_collector.add_class(None)(ClassWithUnionField)
    type_collector.add_function(None)(func_with_list)
    type_collector.add_function(None)(func_with_dict)
    type_collector.add_function(None)(func_with_typed_dict)


    converter = TypescriptConverter(type_collector)

    result = converter.run()
    print(result)
    import pdb;pdb.set_trace()