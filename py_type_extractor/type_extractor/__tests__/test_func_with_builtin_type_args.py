from py_type_extractor.type_extractor.nodes.FunctionFound import FunctionFound
from py_type_extractor.type_extractor.__tests__.utils import cleanup, hash_test
from py_type_extractor.type_extractor.type_extractor import TypeExtractor

import py_type_extractor.test_fixtures.func_with_builtin_type_args as t


module_name = t.__name__

def test_func_with_builtin_type_args():
    type_collector = TypeExtractor()

    type_collector.add(None)(t.func_with_builtin_type_args)

    assert type_collector.classes == {}
    func_found_cleaned = cleanup(
        type_collector.collected_types[
            type_collector.to_collected_types_key(
                module_name=module_name,
                typ_name=t.func_with_builtin_type_args.__qualname__,
            )
        ]
    )
    assert func_found_cleaned == cleanup(FunctionFound(
        name='func_with_builtin_type_args',
        module_name=module_name,
        params={
            'return': int,
            'a': int,
            'b': str,
        },
        doc='',
        return_type=int,
        #
        func=None,
        default_values={
            'b': 'hello',
        },
    ))

    hash_test(type_collector)


if __name__ == '__main__':
    test_func_with_builtin_type_args()