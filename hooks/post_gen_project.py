import logging
from typing import Optional
import stat
from pathlib import Path
import shutil
import subprocess

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("post_gen_project")

ALL_TEMP_FOLDERS = ["licenses", "py_sources"]
PY_SOURCES = Path("py_sources")


def remove(path: Path | str):
    """Remove file or directory if it exists."""
    if isinstance(path, str):
        path = Path(path)
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


if not {{cookiecutter.vscode_settings}}:
    remove(".vscode")

scripts_dir = Path("scripts")

if scripts_dir.exists():
    for script in scripts_dir.glob("**/*.sh"):
        st = script.stat()
        script.chmod(st.st_mode | stat.S_IEXEC)
        logger.info(f"Made executable: {script}")
else:
    logger.info("No scripts/ directory found — skipping chmod step.")


def move_files(
    variant: str,
    save_path: Path,
    source_root: Optional[Path] = None,
    source_file: Optional[Path] = None,
):
    """
    Move files from source_root/variant to save_path
    """
    src_dir = source_root / variant
    if not src_dir.exists():
        logger.warning("No directory found for %s", src_dir)
        return

    logger.info("Moving %s files to %s", variant, save_path)
    logger.info(src_dir)
    for src_path in src_dir.rglob("*"):
        if src_path.is_file():
            logger.info(src_path)
            rel_path = src_path.relative_to(src_dir)
            dst_path = save_path / rel_path
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src_path), str(dst_path))


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        path = Path(folder)
        if path.exists():
            logger.info("Removing temporary folder: %s", path)
            shutil.rmtree(path)


if __name__ == "__main__":
    root = Path.cwd()
    variants = [
        variant
        for variant, condition in [
            ("example_uploads", "{{cookiecutter.include_nomad_example_upload}}"),
            ("apps", "{{cookiecutter.include_nomad_app}}"),
            ("north_tools", "{{cookiecutter.include_north_tools}}"),
        ]
        if condition != "False"
    ]
    if variants:
        module_name = f"pynxtools_{{cookiecutter.reader_name}}"
        src_nomad = root / "src" / module_name / "nomad"
        tests = root / "tests"

        src_nomad.mkdir(parents=True, exist_ok=True)

        # Always copy README.md and __init__.py from py_sources/nomad if any variant is true
        for src_file in (PY_SOURCES / "nomad").iterdir():
            if src_file.is_file():
                shutil.copy(src_file, src_nomad / src_file.name)
                logger.info("Copied %s → %s", src_file, src_nomad / src_file.name)

        for variant in variants:
            # Copy source files
            src_save_path = src_nomad / variant
            src_save_path.mkdir(parents=True, exist_ok=True)
            move_files(variant, src_save_path, PY_SOURCES / "nomad")

            # # Copy test files
            for test_file in (PY_SOURCES / "tests").iterdir():
                if test_file.is_file() and any(
                    variant in test_file.name for variant in variants
                ):
                    dst_file = tests / test_file.name
                    shutil.copy(test_file, dst_file)
                    logger.info("Copied test %s → %s", test_file, dst_file)

            # Copy Test data files
            for test_data_dir in (PY_SOURCES / "tests_data").iterdir():
                if test_data_dir.is_dir() and variant in test_data_dir.name:
                    dst_test_data_dir = root / "tests" / "data" / test_data_dir.name
                    shutil.copytree(test_data_dir, dst_test_data_dir)
                    logger.info(
                        "Copied test data dir %s → %s",
                        test_data_dir,
                        dst_test_data_dir,
                    )
        if "north_tools" not in variants:
            Path.unlink(root / ".dockerignore")
            Path.unlink(root / ".github" / "workflows" / "publish-north.yml")

        remove_temp_folders(ALL_TEMP_FOLDERS)
