from typing import Callable
import inspect

from py_codegen.test_fixtures.func_return_none import func_return_nullable
from py_codegen.test_fixtures.func_not_annotated import func_not_annotated
from py_codegen.test_fixtures.func_with_typed_dict import func_with_typed_dict
from py_codegen.type_extractor.__tests__.test_func_with_typed_dict import test_func_with_typed_dict


def gen_sample_func_doc(func: Callable, test_func: Callable):
    src = ''.join(inspect.getsourcelines(func)[0])
    test_src = ''.join(inspect.getsourcelines(test_func)[0])


    to_write = f'''
    # Example for {func.__qualname__} :
    
    ## Original Source:
    ```python
    {src}
    ```
    
    ## Test:
    ```
    {test_src}
    '''
    return to_write


def save_sample_func_doc(func: Callable, test_func: Callable):
    func_doc = gen_sample_func_doc(func, test_func)
    func_name = func.__qualname__
    open(f'./__samples__/{func_name}.md')

test = save_sample_func(func_with_typed_dict, test_func_with_typed_dict)
