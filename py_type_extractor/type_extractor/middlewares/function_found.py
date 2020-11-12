import inspect
import weakref
from typing import Set

from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor
from py_type_extractor.type_extractor.middlewares.__common__ import remove_temp_options
from py_type_extractor.type_extractor.nodes.BaseOption import BaseOption
from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound


def func_found_middleware(
        func,
        type_extractor: BaseTypeExtractor,
        options: Set[BaseOption],
):
    if not inspect.isfunction(func):
        return None
    try:
        module = inspect.getmodule(func)
        module_name = module.__name__ if module else ''
        filename = module.__file__ if module else ''
        child_options = remove_temp_options(options)

        collected_types_key = f"{module_name}___{func.__qualname__}"
        duplicate_func_found = type_extractor.collected_types.get(collected_types_key)
        if duplicate_func_found is not None:
            assert isinstance(duplicate_func_found, FunctionFound) and duplicate_func_found.func == func
            duplicate_func_found.options = duplicate_func_found.options.union(options)
            return duplicate_func_found

        argspec = inspect.getfullargspec(func)
        signature = inspect.signature(func)


        params = type_extractor.params_to_nodes(
            argspec.annotations,
            argspec.args,
            options=child_options,
        )
        raw_default_values = {
            key: getattr(signature.parameters.get(key), 'default', None)

            for key in argspec.args
        }
        default_values = {
            key: value
            for (key, value) in raw_default_values.items()
            if value is not inspect._empty  # type:ignore
        }
        return_type = type_extractor.rawtype_to_node(
            signature.return_annotation,
            options=child_options,
        )
        func_found = FunctionFound(
            name=func.__name__,
            filePath=filename,
            raw_params=argspec.annotations,
            module_name=module_name,
            default_values=default_values,
            params=params,
            doc=func.__doc__ or '',
            func=func,
            return_type=return_type,
            options=options,
        )

        type_extractor.collected_types[collected_types_key] = func_found
        return weakref.proxy(func_found)
    except Exception as e:
        raise e
