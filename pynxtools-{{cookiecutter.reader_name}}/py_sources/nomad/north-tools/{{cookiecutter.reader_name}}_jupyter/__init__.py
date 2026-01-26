from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

tool = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD and pynxtools plugin {{cookiecutter.__package_name}}.',
    image='ghcr.io/{{cookiecutter.github_username}}/{{cookiecutter.__package_name}}/jupyter:latest',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD and pynxtools plugin {{cookiecutter.__package_name}}.',
    external_mounts=[],
    file_extensions=['ipynb', 'nxs', 'h5', 'hdf5'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': '{{cookiecutter.email}}', 'name': '{{cookiecutter.full_name}}'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='{{cookiecutter.reader_name}}_jupyter',
)

north_tool = NorthToolEntryPoint(id='some_id', north_tool=tool)

{{cookiecutter.reader_name}}_jupyter = NorthToolEntryPoint(
    id_url_safe='{{cookiecutter.module_name}}_{{cookiecutter.reader_name}}', north_tool=tool
)
