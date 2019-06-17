from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import JpgImageFormatter


def python_code_to_jpg(python_code: str, dest_file_path: str):
  result = highlight(python_code, PythonLexer(), JpgImageFormatter())
  with open(dest_file_path, 'wb') as file:
    file.write(result)
