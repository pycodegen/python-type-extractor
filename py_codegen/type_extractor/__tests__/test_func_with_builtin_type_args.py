from py_codegen.type_extractor import TypeExtractor


def test_func_with_builtin_type_args():
    type_collector = TypeExtractor()

    @type_collector.add_function(None)
    def func_with_builtin_args(a: int) -> int:
        return a + 1
    classes_found = type_collector.classes.items()

    import pdb;pdb.set_trace()
    print('type_collector.classes', type_collector.classes)
