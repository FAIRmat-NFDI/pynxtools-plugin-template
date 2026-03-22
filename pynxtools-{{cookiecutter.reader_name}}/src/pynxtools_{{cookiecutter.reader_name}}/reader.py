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
"""{{cookiecutter.technique}} reader built on MultiFormatReader."""

from typing import Any

from pynxtools.dataconverter.readers.multi.reader import MultiFormatReader
from pynxtools.dataconverter.readers.utils import parse_yml


class {{cookiecutter.reader_class}}(MultiFormatReader):
    """
    Reader for {{cookiecutter.technique}} data.

    Pipeline (executed by the inherited ``read()`` method in order):

    1. ``handle_objects`` — process any in-memory Python objects passed by the caller.
    2. Extension dispatch — each input file is routed to the handler registered in
       ``self.extensions`` by file suffix.
    3. ``setup_template`` — return static entries not derived from input files
       (e.g. ``program_name``, fixed calibration constants).
    4. Config file — if ``self.config_file`` is set, it is parsed and ``@attrs`` /
       ``@data`` / ``@eln`` / ``@link`` tokens are resolved via the callbacks.
    5. ``post_process`` — optional hook to modify ``self.config_dict`` dynamically
       and/or return additional template entries.

    Subclass responsibilities:
    - Set ``supported_nxdls`` to the list of NXDL application definitions supported.
    - Register at least one extension handler in ``self.extensions``.
    - Override ``get_attr`` and/or ``get_data`` to expose instrument metadata and
      measurement data to the config-file token system.
    - Override ``setup_template`` for reader-level static entries.
    - Override ``post_process`` for dynamic post-read transformations.

    Optional built-in handlers (register in ``self.extensions`` to activate):
    - ``self.handle_eln_file`` — parses YAML/JSON ELN files; use ``CONVERT_DICT``
      and ``REPLACE_NESTED`` at class level to normalise key names.
    - ``self.set_config_file`` — stores a JSON config file path for ``@``-token
      resolution.
    """

    supported_nxdls = ["{{cookiecutter.supported_nxdl}}"]

    # Map ELN top-level YAML keys to NeXus path fragments (used by handle_eln_file).
    # Keys that already match NeXus path names (e.g. "source", "double_slit") need
    # no entry — only keys that require renaming do.
    CONVERT_DICT: dict[str, str] = {
        "instrument": "INSTRUMENT[instrument]",
    }
    # Replace nested YAML keys with flat NeXus paths (optional).
    REPLACE_NESTED: dict[str, str] = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Parsed data from file handlers — populated by handle_hdf5_file / handle_eln_file.
        self.hdf5_data: dict[str, Any] | None = None
        self.eln_data: dict[str, Any] | None = None

        # Register file-extension handlers here.
        # Keys must be lowercase file suffixes (e.g. ".h5", ".yaml").
        # Each handler receives the file path and must return a dict.
        self.extensions: dict[str, Any] = {
            ".h5": self.handle_hdf5_file,
            ".hdf5": self.handle_hdf5_file,
            ".yaml": self.handle_eln_file,
            ".yml": self.handle_eln_file,
            ".json": self.set_config_file,
        }

    # ------------------------------------------------------------------
    # File handlers — add one per supported input format.
    # ------------------------------------------------------------------

    def handle_hdf5_file(self, file_path: str) -> None:
        """Load HDF5 data into self.hdf5_data as a flat dict {path: value}."""
        # TODO: implement
        return {}
   
    def handle_eln_file(self, file_path: str) -> None:
        self.eln_data = parse_yml(
            file_path,
            convert_dict=self.CONVERT_DICT,
            parent_key="/ENTRY",
        )
        return {}

    # ------------------------------------------------------------------
    # Callbacks — called when the config file contains @attrs / @data / @eln tokens.
    # ------------------------------------------------------------------

    def get_eln_data(self, key: str, path: str) -> Any:
        """Return ELN metadata for ``@eln`` tokens.

        ``parse_yml`` produces flat template-path keys, so look up by ``key``
        (the full NeXus path), not by ``path``.
        """
        # TODO: implement
        return None

    def get_attr(self, key: str, path: str) -> Any:
        """Return instrument metadata from ``self.hdf5_data`` for ``@attrs:path`` tokens.

        ``path`` is the HDF5 dataset path, e.g.
        ``"metadata/instrument/source/wavelength"``.
        """
        # TODO: implement
        return None

    def get_data(self, key: str, path: str) -> Any:
        """Return measurement arrays from ``self.hdf5_data`` for ``@data:path`` tokens.

        ``path`` is the dataset name inside the ``data/`` group, e.g.
        ``"detector_data"``, ``"x_offset"``, ``"interference_data"``.
        """
        # TODO: implement
        return None

    # ------------------------------------------------------------------
    # Optional hooks — override as needed.
    # ------------------------------------------------------------------

    def setup_template(self) -> dict[str, Any]:
        """Return static entries independent of input files."""
        return {}

    def post_process(self) -> dict[str, Any] | None:
        """Post-read hook; may modify self.config_dict and/or return extra entries."""
        return None


READER = {{cookiecutter.reader_class}}
