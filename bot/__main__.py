import os

from .bot import TechStruckBot

os.environ.setdefault("JISHAKU_HIDE", "1")
os.environ.setdefault("JISHAKU_RETAIN", "1")
os.environ.setdefault("JISHAKU_NO_UNDERSCORE", "1")

if __name__ == "__main__":
    from config.bot import bot_config
    from tortoise_config import tortoise_config

    bot = TechStruckBot(tortoise_config=tortoise_config)
    bot.run(bot_config.bot_token)
