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
"""Entry points for {{cookiecutter.__technique}} apps."""

try:
    from nomad.config.models.plugins import AppEntryPoint
    from nomad.config.models.ui import App, Column, Columns, SearchQuantities
except ImportError as exc:
    raise ImportError(
        "Could not import nomad package. Please install the package 'nomad-lab'."
    ) from exc

schema = "pynxtools.nomad.schema.Root"

{{cookiecutter.__nomad_app}} = AppEntryPoint(
    name="{{cookiecutter.__technique}} App",
    description="App for {{cookiecutter.__technique}} data.",
    app=App(
        label="{{cookiecutter.__technique}}",
        path="{{cookiecutter.reader_name}}_app",
        category="Experiment",
        search_quantities=SearchQuantities(
            include=[f"*#{schema}"],
        ),
        filters_locked={
            f"data.ENTRY.definition__field#{schema}": ["{{cookiecutter.supported_nxdl}}"],
        },
        columns=Columns(
            selected=["entry_id"],
            options={
                "entry_id": Column(),
            },
        ),
    ),
)
