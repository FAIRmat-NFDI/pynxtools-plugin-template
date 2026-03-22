# {{cookiecutter.north_tool_name}} - NORTH tool

This directory contains the NORTH tool configuration and Dockerfile for programmatic creation of a NOMAD NORTH tool.

## Quick start

The {{cookiecutter.north_tool_name}} NORTH tool provides a containerized environment for interactive analysis with the {{cookiecutter.__package_name}} plugin.

## Building and testing

Build the Docker image locally from package root:

```bash
docker build -f src/{{cookiecutter.__module_name}}/north_tools/{{cookiecutter.north_tool_name}}/Dockerfile \
	-t ghcr.io/{{cookiecutter.__github_username or cookiecutter.__organization_name}}/{{cookiecutter.__package_name}}:latest .
```

Test the image:

```bash
docker run -p 8888:8888 ghcr.io/{{cookiecutter.__github_username or cookiecutter.__organization_name}}/{{cookiecutter.__package_name}}:latest
```

Access JupyterLab at `http://localhost:8888`.

## Documentation

For comprehensive guidance, you can find information about the `NORTHTool` and `NorthToolEntryPoint` classes in
the [main NOMAD documentation](https://nomad-lab.eu/prod/v1/docs/). These resources cover entry point configuration, image structure, and dependency management.

- [How-to > ... > How to create a NORTH tool](https://nomad-lab.eu/prod/v1/docs/howto/plugins/types/north_tools.html)
- [Reference > ... > NorthToolEntryPoint](https://nomad-lab.eu/prod/v1/docs/reference/plugins.html#northtoolentrypoint)
- [Reference > ... > NORTHTool](https://nomad-lab.eu/prod/v1/docs/reference/config.html#northtool)
