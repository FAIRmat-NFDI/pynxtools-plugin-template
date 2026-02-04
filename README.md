# pynxtools-plugin-template

A cookiecutter template for creating a [`pynxtools`](https://github.com/FAIRmat-NFDI/pynxtools) reader plugin.

## Getting started

Install [`cruft`](https://cruft.github.io/cruft/#installation) and [`cookiecutter`](https://github.com/cookiecutter/cookiecutter).

We recommend to use [`uv`](https://docs.astral.sh/uv/), an etremely fast Python package and project manager:

```bash
uv pip install cruft cookiecutter
```

Installation with standard pip is of course also possible (just omit the starting `uv` in the commands).

## New projects

Run the following command to create a new `pynxtools` plugin project using `pynxtools-plugin-template`:

### Using https

```bash
cruft create https://github.com/FAIRmat-NFDI/pynxtools-plugin-template.git
```

### Using ssh

```bash
cruft create git@github.com:FAIRmat-NFDI/pynxtools-plugin-template.git
```

### Using the GitHub CLI

```bash
cruft create gh:FAIRmat-NFDI/pynxtools-plugin-template.git
```

## Existing projects

You can also link existing `pynxtools` plugin projects to pynxtools-plugin-template using `cruft`.

### Using https

```bash
cruft link https://github.com/FAIRmat-NFDI/pynxtools-plugin-template.git
```

### Using ssh

```bash
cruft link git@github.com:FAIRmat-NFDI/pynxtools-plugin-template.git
```

### Using the GitHub CLI

```bash
cruft link gh:FAIRmat-NFDI/pynxtools-plugin-template.git
```

## Cookiecutter input

Cookiecutter prompts you for information regarding your plugin:

```no-highlight
  [1/10] Name of your reader (short, lowercase, no spaces) (): test
  [2/10] Primary application definition this reader supports (NXtest): NXtest
  [3/10] Short description (): My pynxtools test plugin
  [4/10] Author's full name (): John Doe
  [5/10] Author's email address (fairmat@physik.hu-berlin.de): john.doe@email.com
  [6/10] Select license
    1 - Apache Software License 2.0
    2 - BSD-3
    3 - GNU GPL v3.0+
    4 - MIT
    5 - Mozilla Public License Version 2.0
    Choose from [1/2/3/4/5] (1): 1
  [7/10] Zenodo record (last number in DOI, if available) ():
  [8/10] Include VSCode settings? [y/n] (y): y
  [9/10] Include a NOMAD app entry point? [y/n] (y): y
  [10/10] Include a NOMAD example upload entry point? [y/n] (y): y
INFO:post_gen_project:Copied py_sources/nomad/README.md → /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/src/pynxtools_test/nomad/README.md
INFO:post_gen_project:Copied py_sources/nomad/__init__.py → /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/src/pynxtools_test/nomad/__init__.py
INFO:post_gen_project:Moving example_uploads files to /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/src/pynxtools_test/nomad/example_uploads
INFO:post_gen_project:py_sources/nomad/example_uploads
INFO:post_gen_project:py_sources/nomad/example_uploads/README.md
INFO:post_gen_project:py_sources/nomad/example_uploads/__init__.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_apps.py → /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/tests/test_nomad_apps.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_example_uploads.py → /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/tests/test_nomad_example_uploads.py
INFO:post_gen_project:Moving apps files to /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/src/pynxtools_test/nomad/apps
INFO:post_gen_project:py_sources/nomad/apps
INFO:post_gen_project:py_sources/nomad/apps/__init__.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_apps.py → /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/tests/test_nomad_apps.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_example_uploads.py → /home/lukaspie/fairmat/pynxtools-plugin-template/pynxtools-test/tests/test_nomad_example_uploads.py
INFO:post_gen_project:Removing temporary folder: licenses
INFO:post_gen_project:Removing temporary folder: py_sources
```

There you go - you just created a minimal `pynxtools` plugin.

> [!NOTE]
> In the above prompt, we pressed `y` for NOMAD `apps` and `example_uploads`. This creates two plugin entry points for [`nomad`](https://nomad-lab.eu/): one for a NOMAD app and one for an example upload. This also means that your package becomes a package for the `nomad-lab` package. If installed together, the plugin entry points are detected automatically and can be used directly within NOMAD.

## Staying up to date

We are regularly updating this template with new functionality. To stay up to date, you can run

```bash
cruft update
```

after you have initiated the cruft link.

There is also a GitHub workflow that automatically creates a pull request in your repository if the template has changed (for this to work, your organization must allow automated pull requests.)

In case new features are added to the template that require user input, you can run 

```bash
cruft update -i
```

`i` for --cookiecutter-input to add the new features that require user input.

Check all the generated files, if there are any git conflicts. Conflicting files will appear with name `<filename>.rej`. These conflicts need to be resolved in `<filename>` manually and the `<filename>.rej` file needs to be removed before committing.

## Git

The cookiecutter template will only create the structure of the repository. We strongly recommend using Git for code versioning. After the cruft creation, run

```bash
git init
git add -A
git commit -m "initial commit"
```

to initialize git versioning. If your repository is published to GitHub, this also enables the previously mentioned automated update in the Github Actions.

## What you should implement

The cookiecutter template only creates the basic structure of the repository. In order to have a useful package, there are multiple topics you should address.

- **Write your reader**: In `pynxtoosl-PLUGIN/src/pynxtoos_PLUGIN/reader.py` (where `PLUGIN` is the `cookiecutter.reader_name`), you will find an empty reader. You should implement the reader to parse data from your technique. You can learn more about creating `pynxtools` readers in the [`pynxtools` documentation](https://fairmat-nfdi.github.io/pynxtools/how-tos/pynxtools/build-a-plugin.html#writing-a-reader).
- **Provide test data**: In `pynxtoosl-PLUGIN/`, you will find standardized tests using the [`pynxtools.testing`](https://fairmat-nfdi.github.io/pynxtools/how-tos/pynxtools/using-pynxtools-test-framework.html) module. You should add data in `tests/data` that your reader can use to convert to HDF5 files for the chosen application definition. For each test case, a new folder shall be createad within `tests/data`. In this folder, there should also be a reference NeXus file for comparison in the tests. You can add the name of the folders to the `scripts/generate_reference_files.sh` script to be able to automatically create the reference test file when your reader changes.
- **Documentation**: There is a [`mkdocs`](https://www.mkdocs.org/) template available in the `docs` folder. You should add to the documentation (keeping to the [Diátaxis](https://diataxis.fr/) framework).
- **NOMAD integration**: If you choose to use a NOMAD entry plugin point during package creation with cookiecutter, you should implement these entry points. You can learn more about NOMAD entry points in the [NOMAD documentation](https://nomad-lab.eu/prod/v1/docs/howto/plugins/plugins.html).
- **Spellcheck**: We run spellcheckers using [`cspell`](https://cspell.org/) of both the code and the documentation. The spellchecker is integrated as a [pre-commit hook](https://pre-commit.com/) as well as in an automated GitHub Actions pipeline. When creating your reader, you may use custom words that are in the standard `cspell` dictionaries. In your new plugin, there is a custom dictionary defined in `.cspell/custom-dictionary.txt`. You can automatically update it by running the bash script at `scripts/generate_custom_dict.sh`. Please check the updated custom dictionary after running the script for typos and misspellings.
- **Publish**: Once your reader plugin is working, you should create a release on GitHub. When you release the package on GitHub, it is automatically published on PyPI, provided that you have added a PyPI access token to your repository. For publication to Zenodo, it is also important to fill out the `CITATION.cff` file.
