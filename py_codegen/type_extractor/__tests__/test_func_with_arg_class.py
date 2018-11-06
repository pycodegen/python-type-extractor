from py_codegen.type_extractor import TypeExtractor


def test_func_with_arg_class():
    type_collector = TypeExtractor()

    class ArgClass:
        arg1: str
        arg2: int

    @type_collector.add_function(None)
    def func_with_arg_class(a: ArgClass) -> ArgClass:
        return a
    type_collector.classes.