from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.test_fixtures.func_with_builtin_type_args import func_with_builtin_args

def test_func_with_builtin_type_args():
    type_collector = TypeExtractor()

    type_collector.add_function(None)(func_with_builtin_args)
    classes_found = type_collector.classes.items()

    print('type_collector.classes', type_collector.classes)
