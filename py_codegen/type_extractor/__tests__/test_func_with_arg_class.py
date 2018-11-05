from py_codegen.type_extractor import CollectType


def test_func_with_arg_class():
    type_collector = CollectType()

    class ArgClass:
        arg1: str
        arg2: int

    @type_collector.add_function(None)
    def func_with_arg_class(a: ArgClass) -> ArgClass:
        return a
    classes_found = type_collector.classes.items()

    import pdb;pdb.set_trace()
    print('type_collector.classes', type_collector.classes)

# if __name__ == '__main__':
test_func_with_arg_class()