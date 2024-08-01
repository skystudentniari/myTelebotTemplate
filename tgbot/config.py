from dataclasses import dataclass
from typing import List
from environs import Env


@dataclass
class TgBot:
    token: str
    # admin_ids: List[int]

    @staticmethod
    def from_env(env: Env):
        token = env.str("BOT_TOKEN")
        # admin_ids = env.list("ADMINS", subcast=int)
        # return TgBot(token=token, admin_ids=admin_ids)
        return TgBot(token=token, )


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot.from_env(env))
