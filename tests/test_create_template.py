import shutil
import os
import pytest
import subprocess


def run_tox(plugin):
    """Run the tox suite of the newly created plugin."""
    tox_plugin_path = os.path.join(plugin, "tox.ini")
    shutil.copy("tox.ini", tox_plugin_path)
    command = [
        "tox",
        "--workdir",
        plugin,
        "-c",
        tox_plugin_path,
        "run",
    ]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print("Command Output:")
    print(stdout.decode())
    print(stderr.decode())
    assert process.returncode == 0


@pytest.mark.parametrize("reader_name", ["test"])
@pytest.mark.parametrize("license", [
        "Apache Software License 2.0",
        "BSD-3",
        "GNU GPL v3.0+",
        "MIT",
        "Mozilla Public License Version 2.0"
    ]
)
@pytest.mark.parametrize(
    "include_nomad_app",
    [True, False],
)
@pytest.mark.parametrize(
    "include_nomad_example_upload",
    [True, False],
)
# @pytest.mark.parametrize(
#     "include_nomad_parser",
#     [True, False],
# )
def test_run_cookiecutter_and_plugin_tests(
    cookies,
    reader_name,
    license,
    include_nomad_app,
    include_nomad_example_upload,
    # include_nomad_parser,
):
    """Create a new plugin via cookiecutter and run its tests."""
    result = cookies.bake(
        extra_context={
            "reader_name": reader_name,
            "supported_nxdl": "NXtest",
            "author_name": "John Doe",
            "author_email": "name.surname@physik.hu-berlin.de",
            "license": license,
            "vscode_settings": "True",
            "include_nomad_app": str(include_nomad_app),
            "include_nomad_example_upload": str(include_nomad_example_upload),
            # "include_nomad_parser": str(include_nomad_parser),
        }
    )
    assert result.exit_code == 0
    assert result.exception is None
    
    package_name = result.context["__package_name"]
    module_name = result.context["__module_name"]
    # technique = result.context["__technique"]
    
    assert result.project_path.name == result.context["__package_name"]
    assert result.project_path.is_dir()
    assert result.project_path.joinpath(
        "src", f"{module_name}", "__init__.py"
    ).is_file()

    if include_nomad_app:
        assert result.project_path.joinpath(
            "src", f"{module_name}", "nomad", "apps", "__init__.py"
        ).is_file()
    else:
        assert not result.project_path.joinpath(
            "src",
            f"{module_name}",
            "nomad",
            "apps",
        ).is_dir()
    if include_nomad_example_upload:
        print(result.project_path.joinpath(
            "src", f"{module_name}", "nomad", "example_uploads", "__init__.py"
        ))
        assert result.project_path.joinpath(
            "src", f"{module_name}", "nomad", "example_uploads", "__init__.py"
        ).is_file()
    # else:
    #     assert not result.project_path.joinpath(
    #         "src",
    #         f"{module_name}",
    #         "parsers",
    #     ).is_dir()
    # # if include_nomad_parser:
    # #     assert result.project_path.joinpath(
    # #         "src", f"{module_name}", "nomad", "parsers", "parser.py"
    # #     ).is_file()
    # # else:
    # #     assert not result.project_path.joinpath(
    # #         "src",
    # #         f"{module_name}",
    # #         "parsers",
    # #     ).is_dir()

    if include_nomad_app and include_nomad_example_upload: # and include_nomad_parser:
        run_tox(str(result.project_path))