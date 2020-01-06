import inspect

from typing import Set

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.FunctionFound import FunctionFound


def func_found_middleware(
        func,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not inspect.isfunction(func):
        return None
    try:
        duplicate_func_found = type_extractor.collected_types.get(func.__name__)
        if duplicate_func_found is not None:
            assert isinstance(duplicate_func_found, FunctionFound) and duplicate_func_found.func == func
            duplicate_func_found.options = duplicate_func_found.options.union(options)
            return duplicate_func_found

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
            options=options,
        )

        type_extractor.collected_types[func_found.name] = func_found
        return func_found
    except Exception as e:
        raise e
