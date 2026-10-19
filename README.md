# pynxtools-plugin-template

A cookiecutter template for creating a [`pynxtools`](https://github.com/FAIRmat-NFDI/pynxtools) reader plugin.

## Getting started

Install [`cruft`](https://cruft.github.io/cruft/#installation) and [`cookiecutter`](https://github.com/cookiecutter/cookiecutter).

We recommend to use [`uv`](https://docs.astral.sh/uv/), an extremely fast Python package and project manager:

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
  [1/16] Name of your reader (short, lowercase, no spaces) (): test
  [2/16] Primary application definition this reader supports (NXtest):
  [3/16] Short description (): My pynxtools test plugin
  [4/16] technique (TEST): Test
  [5/16] reader_class (TestReader):
  [6/16] Author's full name (The NOMAD Authors):
  [7/16] Author's email address (fairmat@physik.hu-berlin.de):
  [8/16] GitHub username (used for Docker image, leave empty to use your organization name) (): FAIRmat-NFDI
  [9/16] GitHub organization name (used as fallback if username is not provided). (fairmat-nfdi):
  [10/16] Select license
    1 - Apache Software License 2.0
    2 - BSD-3
    3 - GNU GPL v3.0+
    4 - MIT
    5 - Mozilla Public License Version 2.0
    Choose from [1/2/3/4/5] (1):
  [11/16] Zenodo record (last number in DOI, if available) ():
  [12/16] Include VSCode settings? [y/n] (y): y
  [13/16] Include a NOMAD app entry point? [y/n] (y): y
  [14/16] Include a NOMAD example upload entry point? [y/n] (y): y
  [15/16] Include NOMAD North tool? [y/n] (n): y
  [16/16] Name of the NOMAD North tool, if include NOMAD North tool is 'y' (test): y
INFO:post_gen_project:Made executable: scripts/generate_custom_dict.sh
INFO:post_gen_project:Made executable: scripts/generate_reference_files.sh
INFO:post_gen_project:Copied py_sources/nomad/__init__.py → /home/pynxtools-test/src/pynxtools_test/nomad/__init__.py
INFO:post_gen_project:Moving example_uploads files to /home/pynxtools-test/src/pynxtools_test/nomad/example_uploads
INFO:post_gen_project:py_sources/nomad/example_uploads
INFO:post_gen_project:py_sources/nomad/example_uploads/__init__.py
INFO:post_gen_project:py_sources/nomad/example_uploads/example/README.md
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_apps.py → /home/pynxtools-test/tests/test_nomad_apps.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_example_uploads.py → /home/pynxtools-test/tests/test_nomad_example_uploads.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_north_tools.py → /home/pynxtools-test/tests/test_nomad_north_tools.py
INFO:post_gen_project:Moving apps files to /home/pynxtools-test/src/pynxtools_test/nomad/apps
INFO:post_gen_project:py_sources/nomad/apps
INFO:post_gen_project:py_sources/nomad/apps/__init__.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_apps.py → /home/pynxtools-test/tests/test_nomad_apps.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_example_uploads.py → /home/pynxtools-test/tests/test_nomad_example_uploads.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_north_tools.py → /home/pynxtools-test/tests/test_nomad_north_tools.py
INFO:post_gen_project:Moving north_tools files to /home/pynxtools-test/src/pynxtools_test/nomad/north_tools
INFO:post_gen_project:py_sources/nomad/north_tools
INFO:post_gen_project:py_sources/nomad/north_tools/__init__.py
INFO:post_gen_project:py_sources/nomad/north_tools/y/Dockerfile
INFO:post_gen_project:py_sources/nomad/north_tools/y/README.md
INFO:post_gen_project:py_sources/nomad/north_tools/y/__init__.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_apps.py → /home/pynxtools-test/tests/test_nomad_apps.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_example_uploads.py → /home/pynxtools-test/tests/test_nomad_example_uploads.py
INFO:post_gen_project:Copied test py_sources/tests/test_nomad_north_tools.py → /home/pynxtools-test/tests/test_nomad_north_tools.py
INFO:post_gen_project:Copied test data dir py_sources/tests_data/north_tools → /home/pynxtools-test/tests/data/north_tools
INFO:post_gen_project:Removing temporary folder: licenses
INFO:post_gen_project:Removing temporary folder: py_sourc
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

`-i` for --cookiecutter-input to add the new features that require user input.

Check all the generated files, if there are any git conflicts. Conflicting files will appear with name `<filename>.rej`. These conflicts need to be resolved in `<filename>` manually and the `<filename>.rej` file needs to be removed before committing.

## Git

The cookiecutter template will only create the structure of the repository. We strongly recommend using Git for code versioning. After the cruft creation, run

```bash
git init
git add -A
git commit -m "initial commit"
```

to initialize git versioning. If your repository is published to GitHub, this also enables the previously mentioned automated update in the Github Actions.

## Branching and releases

Generated plugins follow the `develop` / `release/*` / `main` branching model of `pynxtools`:

- `develop`: default branch, all regular PRs target it.
- `release/vX.Y.Z`: created from `develop` for each release.
- `main`: released versions only, receives PRs from `release/*` branches.

The full model and release steps are described in `docs/tutorial/contributing.md` of your plugin.

### One-time GitHub setup

The workflows expect this setup, so do it once after pushing your plugin to GitHub:

1. Create the `develop` branch from `main` and push it:

    ```bash
    git switch -c develop
    git push -u origin develop
    ```

1. Make `develop` the [default branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch).
1. Add a [branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) for `main` and mark the `check-source-branch` job (from `.github/workflows/check-source-is-release.yml`) as a required status check. GitHub only lists a check after it has run once, so open a test PR into `main` first if it does not show up.

Without the `develop` branch, the weekly Cruft update workflow fails, because it checks out and targets `develop`.

### Existing plugins

The Cruft update workflow never changes files in `.github/workflows`. To adopt this model in an existing plugin, copy the workflows from a freshly generated plugin by hand and then do the one-time setup above.

## What you should implement

The cookiecutter template only creates the basic structure of the repository. In order to have a useful package, there are multiple topics you should address.

- **Write your reader**: In `pynxtools-PLUGIN/src/pynxtools_PLUGIN/reader.py` (where `PLUGIN` is the `cookiecutter.reader_name`), you will find an empty reader. You should implement the reader to parse data from your technique. You can learn more about creating `pynxtools` readers in the [`pynxtools` documentation](https://fairmat-nfdi.github.io/pynxtools/how-tos/pynxtools/build-a-plugin.html#writing-a-reader).
- **Provide test data**: In `pynxtools-PLUGIN/`, you will find standardized tests using the [`pynxtools.testing`](https://fairmat-nfdi.github.io/pynxtools/how-tos/pynxtools/using-pynxtools-test-framework.html) module. You should add data in `tests/data` that your reader can use to convert to HDF5 files for the chosen application definition. For each test case, a new folder shall be created within `tests/data`. In this folder, there should also be a reference NeXus file for comparison in the tests. You can add the name of the folders to the `scripts/generate_reference_files.sh` script to be able to automatically create the reference test file when your reader changes.
- **Documentation**: There is a [`mkdocs`](https://www.mkdocs.org/) template available in the `docs` folder. You should add to the documentation (keeping to the [Diátaxis](https://diataxis.fr/) framework).
- **NOMAD integration**: If you choose to use a NOMAD entry plugin point during package creation with cookiecutter, you should implement these entry points. You can learn more about NOMAD entry points in the [NOMAD documentation](https://nomad-lab.eu/prod/v1/docs/howto/plugins/plugins.html).
- **Spellcheck**: We run spellcheckers using [`cspell`](https://cspell.org/) of both the code and the documentation. The spellchecker is integrated as a [pre-commit hook](https://pre-commit.com/) as well as in an automated GitHub Actions pipeline. When creating your reader, you may use custom words that are in the standard `cspell` dictionaries. In your new plugin, there is a custom dictionary defined in `.cspell/custom-dictionary.txt`. You can automatically update it by running the bash script at `scripts/generate_custom_dict.sh`. Please check the updated custom dictionary after running the script for typos and misspellings.
- **Publish**: Once your reader plugin is working, you should create a release on GitHub from a `release/vX.Y.Z` branch (see [Branching and releases](#branching-and-releases)). When you release the package on GitHub, it is automatically published on PyPI, provided that you have added a PyPI access token to your repository. For publication to Zenodo, it is also important to fill out the `CITATION.cff` file.
