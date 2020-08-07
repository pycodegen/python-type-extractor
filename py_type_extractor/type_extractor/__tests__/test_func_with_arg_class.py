from py_type_extractor.type_extractor.__tests__.utils import cleanup, traverse
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor


def test_func_with_arg_class():
    type_collector = TypeExtractor()

    class ArgClass:
        arg1: str
        arg2: int

    @type_collector.add(None)
    def func_with_arg_class(a: ArgClass) -> ArgClass:
        return a

    func_found_cleaned = traverse(
        type_collector.collected_types['func_with_arg_class'],
        cleanup,
    )
    arg_class_found = ClassFound(
        name='ArgClass',
        fields={
            'arg1': str,
            'arg2': int,
        },
    )
    assert func_found_cleaned == cleanup(
        FunctionFound(
            name='func_with_arg_class',
            params={
                'return': arg_class_found,
                'a': arg_class_found,
            },
            doc='',
            return_type=arg_class_found,
            #
            func=None,
            filePath=None,
            raw_params=None,
        )
    )
