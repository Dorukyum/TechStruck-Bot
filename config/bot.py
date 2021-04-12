from pydantic import BaseSettings


class BotConfig(BaseSettings):
    bot_token: str
    quiz_api_token: str
    log_webhook: str

    class Config:
        env_file = ".env"


bot_config = BotConfig()
