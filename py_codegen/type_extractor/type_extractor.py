import builtins
import inspect
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable, Dict

from .ClassFound import ClassFound
from .DuplicateNameFound import DuplicateNameFound
from .FunctionFound import FunctionFound

def is_builtin(something):
    return inspect.getmodule(something) is not builtins

class CollectType:
    functions: Dict[str, FunctionFound] = dict()

    classes: Dict[str, ClassFound] = dict()

    def add_function(self, options):
        def add_function_decoration(func: Callable):
            signature = inspect.getfullargspec(func)
            self.__process_params(signature.annotations)
            function_found = self.__to_function_found(func)
            if function_found.name in self.functions:
                raise DuplicateNameFound(
                    self.functions.get(
                        function_found.name
                    ),
                    function_found
                )
            self.functions[function_found.name] = function_found
            # import pdb; pdb.set_trace()
            return func
        return add_function_decoration

    def __process_params(self, params: OrderedDict):
        processed_params = dict()
        for key, value in params.items():
            if inspect.isclass(value) and not is_builtin(value):
                class_found = self.__to_class_found(value)
                processed_params[key] = class_found
            if inspect.isfunction(value):
                function_found = self.__to_function_found(value)
                processed_params[key] = function_found
            print("key", key, " / value", value)
        return processed_params

    def __to_class_found(self, _class):
        _data_class = dataclass(_class)
        argspec = inspect.getfullargspec(_data_class)
        module = inspect.getmodule(_class)
        filename = module.__file__
        fields = self.__process_params(argspec.annotations)
        class_found = ClassFound(
            name=_class.__name__,
            filePath=filename,
            raw_fields=argspec.annotations,
            fields=fields,
            doc=_class.__doc__
        )
        return class_found

    def __to_function_found(self, func: Callable) -> FunctionFound:
        argspec = inspect.getfullargspec(func)
        signature = inspect.signature(func)
        module = inspect.getmodule(func)
        filename = module.__file__
        params = self.__process_params(argspec.annotations)
        func_found = FunctionFound(
            name=func.__name__,
            filePath=filename,
            raw_params=argspec.annotations,
            params=params,
            doc=func.__doc__,
            func=func,
            return_type=signature.return_annotation,
        )
        return func_found

    def __to_dictionary_key(self, obj):
        module = inspect.getmodule(obj)
        filename = module.__file__
        return obj.__name + '::' + filename

    def add_class(self, options):
        def add_class_decoration(_class):
            class_found = self.__to_class_found(_class)
            self.classes[self.__to_dictionary_key(_class)] = class_found
            import pdb;pdb.set_trace()
        return add_class_decoration

    # def get_classes(self):
