from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    database_url: str = Field(..., alias="DATABASE_URL")
    jwt_secret_key: str = Field(..., alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    kakao_client_id: str = Field(..., alias="KAKAO_CLIENT_ID")
    kakao_redirect_uri: str = Field(..., alias="KAKAO_REDIRECT_URI")

    class Config:
        env_file = ".env"
        case_sensitive = False  # 선택사항, 대소문자 구분 안 할 경우

settings = Settings()
