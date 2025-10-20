from typing import Any

from pynxtools.dataconverter.readers.base.reader import BaseReader

class {{cookiecutter.reader_class}}(BaseReader):
    """
    Reader for my method....
    PLEASE UPDATE
    """

    supported_nxdls = ["{{cookiecutter.supported_nxdls}}"]

    def read(
        self,
        template: dict | None = None,
        file_paths: tuple[str] | None = None,
        objects: tuple[Any] | None = None,
    ):
        """
        General read menthod to prepare the template.
        """
        return template


READER = {{cookiecutter.reader_class}}
