from pydantic_settings import BaseSettings, SettingsConfigDict


class PachkaIntegrationSettings(BaseSettings):
        access_token: str
        user_id: int

        model_config = SettingsConfigDict(env_file='.env')


settings = PachkaIntegrationSettings()