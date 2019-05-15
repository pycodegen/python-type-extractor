from typing import Callable

from py_codegen.plugins.typescript.Converter import TypescriptConverter

from py_codegen.test_fixtures.union_type_class import ClassWithUnionField
from py_codegen.test_fixtures.func_with_dict import func_with_dict
from py_codegen.test_fixtures.func_with_list import func_with_list
from py_codegen.test_fixtures.func_with_typed_dict import func_with_typed_dict
from py_codegen.test_fixtures.func_not_annotated import func_not_annotated
from py_codegen.test_fixtures.func_return_none import func_return_nullable
from py_codegen.test_fixtures.func_with_tuple import func_with_tuple
from py_codegen.test_fixtures.func_with_literals import func_with_literals
from py_codegen.test_fixtures.func_with_mapping import func_with_mapping

from py_codegen.type_extractor.type_extractor import TypeExtractor

from os import path

def generate_and_write_ts_definition(func_or_cls):
    type_collector = TypeExtractor()
    type_collector.add(None)(func_or_cls)
    converter = TypescriptConverter(type_collector)
    __write_ts_definition__(func_or_cls.__qualname__, converter.run())


def __write_ts_definition__(name: str, definition_str: str):

    with open(f'{path.dirname(path.abspath(__file__))}/ts_generated/{name}.d.ts', 'w+') as file:
        file.write(definition_str)

# classes
generate_and_write_ts_definition(ClassWithUnionField)

# functions
generate_and_write_ts_definition(func_with_dict)
generate_and_write_ts_definition(func_with_list)
generate_and_write_ts_definition(func_with_typed_dict)
generate_and_write_ts_definition(func_not_annotated)
generate_and_write_ts_definition(func_return_nullable)
generate_and_write_ts_definition(func_with_tuple)
generate_and_write_ts_definition(func_with_literals)
generate_and_write_ts_definition(func_with_mapping)
