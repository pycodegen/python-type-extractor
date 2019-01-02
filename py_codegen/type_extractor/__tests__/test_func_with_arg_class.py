from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_func_with_arg_class():
    type_collector = TypeExtractor()

    class ArgClass:
        arg1: str
        arg2: int

    @type_collector.add_function(None)
    def func_with_arg_class(a: ArgClass) -> ArgClass:
        return a

    classes = type_collector.classes
    classes_list = classes.values()
    functions = type_collector.functions
    functions_list = functions.values()

    assert(classes_list.__len__() == 1)
    assert (functions_list.__len__() == 1)
