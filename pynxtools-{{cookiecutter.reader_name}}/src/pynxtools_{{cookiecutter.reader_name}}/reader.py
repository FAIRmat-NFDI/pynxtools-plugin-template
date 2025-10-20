from typing import Any, Tuple

from pynxtools.dataconverter.readers.base.reader import BaseReader

class {{cookiecutter.reader_class}}(BaseReader):
    """
    Reader for my method....
    PLEASE UPDATE
    """

    supported_nxdls = ["{{cookiecutter.supported_nxdls}}"]

    def read(
        self,
        template: dict = None,
        file_paths: Tuple[str] = None,
        objects: Tuple[Any] = None,
    ):
        """
        General read menthod to prepare the template.
        """
        return template


READER = {{cookiecutter.reader_class}}
