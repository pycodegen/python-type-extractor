import builtins
import inspect


def is_builtin(something):
    return inspect.getmodule(something) is builtins