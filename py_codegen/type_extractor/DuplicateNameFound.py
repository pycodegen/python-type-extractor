import typing
from .ClassFound import ClassFound
from .FunctionFound import FunctionFound

class DuplicateNameFound(Exception):
  def __init__(
    self,
    found1: typing.Union[ClassFound, FunctionFound],
    found2: typing.Union[ClassFound, FunctionFound],
  ):
    pass
