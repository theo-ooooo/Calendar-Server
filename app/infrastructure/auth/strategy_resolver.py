from app.domain.auth.provider_type import Provider
from app.domain.auth.social_strategy import SocialLoginStrategy
from app.infrastructure.auth.kakao_strategy import KakaoAuthStrategy


def get_social_strategy(provider:Provider) -> SocialLoginStrategy:
    if provider == Provider.kakao:
        return KakaoAuthStrategy()

    raise ValueError(f"지원하지 않은 소셜: {provider} ")