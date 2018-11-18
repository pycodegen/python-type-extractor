from py_codegen.plugins.typescript import TypescriptConverter
from py_codegen.test_fixtures.func_with_builtin_type_args import func_with_builtin_args
from py_codegen.type_extractor.type_extractor import TypeExtractor
def test_builtin_args():
    type_collector = TypeExtractor()
    type_collector.add_function(None)(func_with_builtin_args)
    # converted = convert_to_typescript(type_collector)