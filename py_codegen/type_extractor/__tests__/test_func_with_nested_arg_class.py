from py_codegen.type_extractor import TypeExtractor


def test_func_with_nested_arg_class():
    type_collector = TypeExtractor()

    class ChildClass:
        carg1: str

    class ParentClass:
        parg1: str
        parg2: ChildClass

    @type_collector.add_function(None)
    def func_with_nested_arg_class(a: ParentClass) -> ParentClass:
        return a

    classes = type_collector.classes
    classes_list = classes.values()
    functions = type_collector.functions
    functions_list = functions.values()

    assert (classes_list.__len__() == 2)
    assert (functions_list.__len__() == 1)
