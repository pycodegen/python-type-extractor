from py_type_extractor.type_extractor.__base__ import BaseTypeExtractor


def hash_test(type_extractor: BaseTypeExtractor):
    for (key, value) in type_extractor.collected_types.items():
        try:
            hashed = hash(value)
            print(hashed)
        except Exception as e:
            raise RuntimeError(f"Hash failed -- couldn't hash {key} of {value}")