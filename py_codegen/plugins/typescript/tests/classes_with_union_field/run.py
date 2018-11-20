import sys
import os

current_dir = os.path.dirname(__file__)

def to_parent_dir(path_str: str, iter: int):
    if (iter == 0):
        return path_str
    return to_parent_dir(
        os.path.join(path_str, os.pardir),
        iter - 1,
    )


parent_dir = os.path.abspath(to_parent_dir(__file__, 6))

sys.path.append(parent_dir)

# noinspection PyPep8
from py_codegen.test_fixtures.union_type_class import ClassWithUnionField
from py_codegen.type_extractor.type_extractor import TypeExtractor
from py_codegen.plugins.typescript.typescript import TypescriptConverter


# noinspection PyPep8

def run():
    type_extractor = TypeExtractor()
    type_extractor.add_class(None)(ClassWithUnionField)

    ts_converter = TypescriptConverter()
    result1 = ts_converter.convert_class_found(type_extractor.classes.get('ClassWithUnionField'))
    save_file_path = os.path.abspath(os.path.join(__file__, os.pardir, 'generated.d.ts'))
    f = open(save_file_path, 'w')
    f.write(result1)
    f.close()


run()
