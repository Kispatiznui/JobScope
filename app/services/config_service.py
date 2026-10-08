import json
from app.core.config import get_config_path



def load_config(filename: str) -> dict:
    path = get_config_path(filename)

    if not path.exists():
        raise FileNotFoundError(
            f"No existe el archivo de configuración: {path}"
        )

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_profile() -> dict:
    return load_config("profile.json")


def load_keywords() -> dict:
    return load_config("keywords.json")


def load_sources() -> dict:
    return load_config("sources.json")