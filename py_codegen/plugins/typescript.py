from py_codegen.type_extractor.type_extractor import TypeExtractor, is_builtin

def convert_builtin_types(builtin_type):
    assert is_builtin(builtin_type)


def extract_class_to_interfaces(collected_types: TypeExtractor) -> str:
    interfaces = collected_types.classes
    return ''
