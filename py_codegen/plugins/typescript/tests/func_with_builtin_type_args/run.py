from py_codegen.test_fixtures.func_with_builtin_type_args import func_with_builtin_args
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.plugins.typescript.typescript import TypescriptConverter

def run():
    type_extractor = TypeExtractor()
    type_extractor.add_function(None)(func_with_builtin_args)
    to_save = open('generated.ts', 'w+')
    to_save.write('''
        test!
    ''')

    ts_converter = TypescriptConverter()
    ts_converter.convert_class_found()
