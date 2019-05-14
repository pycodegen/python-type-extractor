import inspect

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound


def func_found_middleware(func, type_extractor: BaseTypeExtractor):
    if not inspect.isfunction(func):
        return None
    try:
        argspec = inspect.getfullargspec(func)
        signature = inspect.signature(func)
        module = inspect.getmodule(func)
        filename = module.__file__
        params = type_extractor.params_to_nodes(argspec.annotations, argspec.args)
        return_type = type_extractor.rawtype_to_node(signature.return_annotation)
        func_found = FunctionFound(
            name=func.__name__,
            filePath=filename,
            raw_params=argspec.annotations,
            params=params,
            doc=func.__doc__ or '',
            func=func,
            return_type=return_type,
        )
        duplicate_func_found = type_extractor.collected_types.get(func_found.name)
        assert duplicate_func_found == func_found or duplicate_func_found is None
        type_extractor.collected_types[func_found.name] = func_found
        return func_found
    except Exception as e:
        raise e
