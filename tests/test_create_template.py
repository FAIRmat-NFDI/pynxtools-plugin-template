import shutil
import os
import pytest
import subprocess


def run_tox(plugin_path: str):
    """Run the tox suite of the newly created plugin."""
    tox_plugin_path = os.path.join(plugin_path, "tox.ini")
    shutil.copy("tox.ini", tox_plugin_path)
    command = [
        "tox",
        "--workdir",
        plugin_path,
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


def initialize_git(project_path: str):
    """Initialize a Git repository so setuptools_scm can determine version."""
    subprocess.run(["git", "config", "--global", "user.email", "you@example.com"], cwd=project_path, check=True)
    subprocess.run(["git", "config", "user.email", "ci@example.com"], cwd=project_path, check=True)
    subprocess.run(["git", "config", "user.name", "CI Bot"], cwd=project_path, check=True)
    subprocess.run(["git", "init"], cwd=project_path, check=True)
    subprocess.run(["git", "add", "."], cwd=project_path, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_path, check=True)


@pytest.mark.parametrize("reader_name", ["test"])
@pytest.mark.parametrize("license", [
    "Apache Software License 2.0",
    "BSD-3",
    "GNU GPL v3.0+",
    "MIT",
    "Mozilla Public License Version 2.0"
])
@pytest.mark.parametrize("include_nomad_app", [True, False])
@pytest.mark.parametrize("include_nomad_example_upload", [True, False])
def test_run_cookiecutter_and_plugin_tests(
    cookies,
    reader_name,
    license,
    include_nomad_app,
    include_nomad_example_upload,
):
    """Create a new plugin via cookiecutter, initialize Git, and run its tests."""
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
        }
    )
    assert result.exit_code == 0
    assert result.exception is None

    project_path = str(result.project_path)
    package_name = result.context["__package_name"]
    module_name = result.context["__module_name"]

    # Basic structure checks
    assert result.project_path.name == package_name
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("src", module_name, "__init__.py").is_file()

    if include_nomad_app:
        assert result.project_path.joinpath("src", module_name, "nomad", "apps", "__init__.py").is_file()
    else:
        assert not result.project_path.joinpath("src", module_name, "nomad", "apps").is_dir()

    if include_nomad_example_upload:
        assert result.project_path.joinpath("src", module_name, "nomad", "example_uploads", "__init__.py").is_file()

    # Initialize Git so setuptools_scm can determine the version
    initialize_git(project_path)

    # Only run tox if the project has any of the Nomad components
    if include_nomad_app or include_nomad_example_upload:
        run_tox(project_path)
