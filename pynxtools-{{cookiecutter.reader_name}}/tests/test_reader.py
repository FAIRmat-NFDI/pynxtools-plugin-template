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
"""Tests for the pynxtools reader plugin."""

import os
from typing import Any, Literal

import pytest
from pynxtools.dataconverter.convert import get_reader
from pynxtools.testing.nexus_conversion import ReaderTest

READER_NAME = "{{cookiecutter.reader_name}}"
READER_CLASS = get_reader(READER_NAME)
NXDLS = READER_CLASS.supported_nxdls

# Define lines/sections to be ignored in _all_ test cases
ignore_lines_all_tests: list = []
ignore_sections_all_tests: dict = {}

# Test cases should be [("folder", ignore_lines, ignore_sections, "test-id")]
test_cases: list[tuple[str, list[Any], dict[Any, Any], str]] = [
    ("folder", [], {}, "test-id"),
]

test_params: list[Any] = []
for test_case in test_cases:
    for nxdl in NXDLS:
        test_params += [
            pytest.param(
                nxdl,
                test_case[0],
                test_case[1],
                test_case[2],
                id=f"{test_case[3]}-{nxdl.lower()}",
            )
        ]


@pytest.mark.parametrize(
    "nxdl, sub_reader_data_dir, ignore_lines, ignore_sections",
    test_params,
)
def test_nexus_conversion(
    nxdl, sub_reader_data_dir, ignore_lines, ignore_sections, tmp_path, caplog
):
    """
    Test {{cookiecutter.__technique}} reader

    Parameters
    ----------
    nxdl : str
        Name of the NXDL application definition that is to be tested by
        this reader plugin.
    sub_reader_data_dir : str
        Test data directory that contains all the files required for running the data
        conversion through one of the sub-readers. All of these data dirs
        are placed within tests/data/...
    ignore_lines: Dict[str, List[str]]
        Lines within the log files to ignore.
    ignore_sections: Dict[str, List[str]]
        Subsections of the log files to ignore.
    tmp_path : pathlib.PosixPath
        Pytest fixture variable, used to clean up the files generated during
        the test.
    caplog : _pytest.logging.LogCaptureFixture
        Pytest fixture variable, used to capture the log messages during the
        test.

    Returns
    -------
    None.

    """
    caplog.clear()

    files_or_dir = os.path.join(
        *[os.path.dirname(__file__), "data", sub_reader_data_dir]
    )

    ignore_lines: list[str] = ignore_lines_all_tests + ignore_lines
    ignore_sections: dict[str, list[str]] = ignore_sections_all_tests | ignore_sections

    test = ReaderTest(
        nxdl=nxdl,
        reader_name=READER_NAME,
        files_or_dir=files_or_dir,
        tmp_path=tmp_path,
        caplog=caplog,
    )
    test.convert_to_nexus(caplog_level="WARNING", ignore_undocumented=True)
    test.check_reproducibility_of_nexus(
        ignore_lines=ignore_lines, ignore_sections=ignore_sections
    )
