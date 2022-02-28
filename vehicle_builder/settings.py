from typing import Dict
from environs import Env

env = Env()
env.read_env()


def get_config() -> Dict:
    config = {
        "HOST": env.str("HOST", "localhost"),
        "PORT": env.int("PORT", 8080),
        "database": {
            "database": env.str("DATABASE", "postgres"),
            "user": env.str("DB_USER", "postgres"),
            "password": env.str("DB_PASSWORD", "pass"),
            "host": env.str("DB_HOST", "localhost"),
            "port": env.int("DB_PORT", 5432),
        }
    }
    return config
