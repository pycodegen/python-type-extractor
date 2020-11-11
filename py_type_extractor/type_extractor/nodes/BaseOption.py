import abc


class BaseOption(metaclass=abc.ABCMeta):
    pass


class BaseTempOption(
    BaseOption,
    metaclass=abc.ABCMeta,
):
    pass
