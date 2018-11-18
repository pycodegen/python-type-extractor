import sys
from typing import Dict, TypeVar

from py_codegen.type_extractor import TypeOR
from py_codegen.type_extractor.type_extractor import TypeExtractor, is_builtin, ClassFound, FunctionFound

class TypescriptConverter:

    @staticmethod
    def __convert_builtin_types(builtin_type) -> str:
        assert is_builtin(builtin_type)

        if builtin_type == int or builtin_type == float:
            return 'number'

        if builtin_type == str:
            return 'string'

    def __convert_union(self, union_type: TypeOR):
        pass

    # Note: for getting type annotations, not class declarations
    def convert_type_to_text(self, some_type):
        if is_builtin(some_type):
            return self.__convert_builtin_types(some_type)
        if isinstance(some_type, TypeOR):
            return self.__convert_union(some_type)
        if isinstance(some_type, ClassFound):
            return

    def extract_class_to_interfaces(self, collected_types: TypeExtractor) -> str:
        interfaces: Dict[str, str] = {}
        for (key, value) in collected_types.classes.items():
            sys.stderr.write(key)

        # interfaces = collected_types.classes
        # return ''
        import pdb;pdb.set_trace()


    def extract_functions(type_extractor: TypeExtractor):
        function_codes: Dict[str, str] = {}
        # for (key, value) in type_extractor.functions.items():

    def get_class_name(class_found: ClassFound) -> str:
        return class_found.name


    def get_function_name(function_found: FunctionFound) -> str:
        return function_found.name


    def convert_to_typescript(type_extractor: TypeExtractor):
        extract_class_to_interfaces(type_extractor)