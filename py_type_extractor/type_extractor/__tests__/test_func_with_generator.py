import py_type_extractor.test_fixtures.func_with_generator as t
# from py_type_extractor.type_extractor.__tests__.utils import traverse, cleanup, hash_test
# from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
# from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
# from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
# from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound
from py_type_extractor.type_extractor.type_extractor import TypeExtractor


module_name = t.__name__


def test_fun_with_generator():
    type_extractor = TypeExtractor()
    type_extractor.add()(t.some_func_with_generator)
    print(type_extractor)