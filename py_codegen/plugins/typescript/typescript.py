from py_codegen.type_extractor.TypeOR import TypeOR
from py_codegen.type_extractor.type_extractor import ClassFound, FunctionFound, is_builtin
from enum import Enum, auto
from textwrap import dedent


class TypescriptClassFoundConversions(Enum):
    INTERFACE = auto()
    CLASS = auto()


class TypescriptConverter:
    def __get_class_found_type(self, class_found: ClassFound) -> TypescriptClassFoundConversions:
        # TODO: read metadata from class_found to decide
        return TypescriptClassFoundConversions.INTERFACE

    def __get_class_found_name(self, class_found: ClassFound):
        result_type = self.__get_class_found_type(class_found)
        if result_type == TypescriptClassFoundConversions.INTERFACE:
            return f'I{class_found.name}'
        return f'{class_found.name}'

    def convert_class_found(self, class_found: ClassFound):
        if self.__get_class_found_type(class_found) == TypescriptClassFoundConversions.CLASS:
            return self.to_ts_class(class_found)
        return self.to_ts_interface(class_found)

    def to_ts_interface(self, class_found: ClassFound):
        field_type_signatures = '\n'.join(
            list({
                key: f'{key}: {self.to_ts_type_signature(value)};'
                for key, value in class_found.fields.items()
            }.values())
        )
        return dedent(f'''
        export interface {self.__get_class_found_name(class_found)} {{
            {field_type_signatures}
        }}
        ''')

    def to_ts_class(self, class_found: ClassFound):
        field_type_signatures = {
            key: f'{key}: {self.to_ts_type_signature(value)}'
            for key, value in class_found.fields.items()
        }.values()
        dedent(f"""
        class {self.__get_class_found_name(class_found)} {{
            
        }}
        """)

    def to_ts_builtin(self, builtin):
        # TODO: use metadata to generate 'bigint' / etc
        if builtin == str:
            return 'string'
        elif builtin == int:
            return 'number'
        elif builtin == bool:
            return 'boolean'

    def convert_func_found(self, func_found: FunctionFound):
        pass

    def to_ts_type_signature(self, something) -> str:
        if isinstance(something, ClassFound):
            return self.__get_class_found_name(something)
        if isinstance(something, TypeOR):
            name_a = self.to_ts_type_signature(something.a)
            name_b = self.to_ts_type_signature(something.b)
            return f'{name_a} | {name_b}'
        if is_builtin(something):
            return self.to_ts_builtin(something)
