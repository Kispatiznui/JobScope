from pathlib import Path


CONFIG_DIR = Path("config")


def get_config_path(filename: str) -> Path:
    return CONFIG_DIR / filename