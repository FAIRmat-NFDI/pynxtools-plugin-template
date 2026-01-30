"""Tests for the NOMAD NORTH tool."""

import pytest

try:
    import nomad  # noqa: F401
except ImportError:
    pytest.skip(
        "Skipping NOMAD NORTH tool tests because nomad-lab is not installed",
        allow_module_level=True,
    )


def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from {{cookiecutter.__module_name}}.nomad.north_tools.{{cookiecutter.north_tool_name}} import (
        {{cookiecutter.__north_tool_EP_name}},
    )

    assert (
        {{cookiecutter.__north_tool_EP_name}}.id_url_safe == '{{cookiecutter.__module_name}}_{{cookiecutter.reader_name}}'
        or {{cookiecutter.__north_tool_EP_name}}.id == 'nomad-north-{{cookiecutter.reader_name}}'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
