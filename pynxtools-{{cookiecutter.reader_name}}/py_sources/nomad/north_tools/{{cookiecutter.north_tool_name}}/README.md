# pynxtools-{{cookiecutter.reader_name}} - NORTH Jupyter tool

This directory contains the NORTH tool configuration and Docker file for programmatic creation of a Jupyter-based NOMAD NORTH tool.

## Quick start

The {{cookiecutter.north_tool_name}} NORTH tool provides a containerized JupyterLab environment for interactive analysis with the {{cookiecutter.__package_name}} plugin.

## Building and testing

Build the Docker image locally from package root:

```bash
docker build -f src/{{cookiecutter.__module_name}}/north_tools/{{cookiecutter.north_tool_name}}/Dockerfile \
	-t ghcr.io/{{cookiecutter.organization_name or cookiecutter.github_username}}/{{cookiecutter.__package_name}}:latest .
```

Test the image:

```bash
docker run -p 8888:8888 ghcr.io/{{cookiecutter.organization_name or cookiecutter.github_username}}/{{cookiecutter.__package_name}}:latest
```

Access JupyterLab at `http://localhost:8888`.

## Documentation

For comprehensive guidance, see the main docs and the single source of truth for NORTHTool and NorthToolEntryPoint. These resources cover entry point configuration, image structure, and dependency management.

- [NOMAD NORTH tools](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html)
- [Reference for NorthToolEntryPoint](https://fairmat-nfdi.github.io/nomad-docs/reference/plugins.html#northtoolentrypoint)
- [Reference for NORTHTool](https://fairmat-nfdi.github.io/nomad-docs/howto/plugins/types/north_tools.html#north-tool-entry-point)