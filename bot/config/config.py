from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_ID: str = '0002CbsR'

    USE_RANDOM_DELAY_IN_RUN: bool = False
    RANDOM_DELAY_IN_RUN: list[int] = [0, 41000]

    POINTS_COUNT: list[int] = [450, 600]
    AUTO_PLAY_GAME: bool = True
    AUTO_TASK: bool = True
    AUTO_DAILY_REWARD: bool = True
    AUTO_CLAIM_STARS: bool = True
    AUTO_CLAIM_COMBO: bool = True
    AUTO_RANK_UPGRADE: bool = True

    SLEEP_TIME: list[int] = [21000, 32000]

settings = Settings()

