from daily_ai_learning.paths import Paths
from daily_ai_learning.settings import Settings


def test_settings_loads_default():
    paths = Paths.discover()
    settings = Settings.load(paths)
    assert settings.lessons_per_run >= 1
    assert settings.git_branch == "main"


def test_root_discovery_returns_repo_root():
    paths = Paths.discover()
    assert (paths.root / "pyproject.toml").exists()
    assert (paths.root / "config").exists()
