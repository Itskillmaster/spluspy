"""Dependency-light structural tests for the source distribution."""
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "spluspy"


def test_all_python_files_parse():
    files = list(PACKAGE.rglob("*.py"))
    assert files, "package source files must exist"
    for path in files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_public_entry_points_exist():
    assert (PACKAGE / "selfbot" / "__init__.py").is_file()
    assert (PACKAGE / "bot" / "__init__.py").is_file()
    selfbot = (PACKAGE / "selfbot" / "__init__.py").read_text(encoding="utf-8")
    bot = (PACKAGE / "bot" / "__init__.py").read_text(encoding="utf-8")
    assert "Client = SoroushClient" in selfbot
    assert "Bot = Robot" in bot
    assert "BotClient = Robot" in bot


def test_package_metadata_has_runtime_dependencies():
    metadata = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    for dependency in ("aiohttp", "pyaes", "pydantic"):
        assert f'"{dependency}' in metadata


def test_docs_and_examples_exist():
    for relative in (
        "README.md",
        "docs/ARCHITECTURE.md",
        "docs/API_REFERENCE.md",
        "docs/DEVELOPMENT.md",
        "docs/METHODS_CATALOG.md",
        "examples/official_bot.py",
        "examples/selfbot_entry.py",
    ):
        assert (ROOT / relative).is_file(), relative


def test_root_import_is_lazy_and_official_bot_surface_loads():
    import spluspy
    from spluspy.bot import Bot, BotClient, Robot, filters

    assert spluspy.__version__ == "2.2.13"
    assert Bot is Robot
    assert BotClient is Robot
    assert filters is not None
