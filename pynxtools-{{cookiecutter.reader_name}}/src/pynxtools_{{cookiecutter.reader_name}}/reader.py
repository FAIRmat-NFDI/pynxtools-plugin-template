#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any

from pynxtools.dataconverter.readers.base.reader import BaseReader
from {{cookiecutter.__module_name}}.utils.versioning import get_pynxtools_plugin_version


class {{cookiecutter.reader_class}}(BaseReader):
    """Reader for {{cookiecutter.technique}}."""

    supported_nxdls = ["{{cookiecutter.supported_nxdl}}"]

    def read(
        self,
        template: dict | None = None,
        file_paths: tuple[str] | None = None,
        objects: tuple[Any] | None = None,
    ):
        """
        Read method to prepare the template.
        """

        # the dataconverter of the pynxtools core package stores its version
        # under creator and creator_version within the NeXus/HDF5 file's NXroot instance
        # begin of example code how to also store the version of the actual pynxtools-plugin used follows
        entry_id = 1  # changeme
        template_path_prefix = f"/ENTRY[entry{entry_id}]/CS_PROFILING[profiling]/PROGRAM[program1]"
        template[f"{template_path_prefix}/program"] = f"pynxtools_{{cookiecutter.reader_name}}"
        template[f"{template_path_prefix}/program/@version"] = f"{get_pynxtools_plugin_version()}"
        # end of example code

        return template


READER = {{cookiecutter.reader_class}}
