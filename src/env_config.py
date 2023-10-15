from attr import dataclass
from dotenv import load_dotenv
import os

@dataclass
class EnvConfig:
    openai_api_key: str

instance: EnvConfig | None = None

def load_env_config() -> EnvConfig:
    global instance
    if instance is None:
        load_dotenv()
        instance = EnvConfig(
            openai_api_key=get_str("OPENAI_API_KEY")
        )

    return instance

#Same type, except key should only be from EnvConfig
def get_str(key: str) -> str:
    return __ensure(key)

def __ensure(key: str) -> None:
    if os.getenv(key) is None:
        raise ValueError(f"Missing environment variable: {key}")