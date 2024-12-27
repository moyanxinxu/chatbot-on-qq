import os
from dataclasses import asdict, dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class GEMINI_CONFIG:
    """gemini模型的配置"""

    model: str = os.getenv("GEMINI_MODEL_NAME")

    def todict(self) -> dict:
        return asdict(self)


@dataclass
class OPENAI_CONFIG:
    """openai模型的配置"""

    model: str = os.getenv("OPENAI_MODEL_NAME")

    def todict(self) -> dict:
        return asdict(self)


@dataclass
class CLIENT_CONFIG:
    """qq机器人的密钥"""

    appid: str = os.getenv("appid")
    secret: str = os.getenv("secret")

    def todict(self) -> dict:
        return asdict(self)
