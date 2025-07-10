# app/api/v1/auth/router.py
from fastapi import APIRouter, Query, Depends, HTTPException
from fastapi.params import Header
from starlette.responses import RedirectResponse
from starlette.status import HTTP_200_OK
import logging

from app.api.v1.auth.schema import TokenResponse
from app.api.v1.auth.dependencies import (
    get_create_token_use_case,
    get_reissue_token_use_case,
    get_social_user_use_case
)
from app.domain.auth.entity.provider_type import Provider
from app.infrastructure.config import settings
from app.usecases.auth.create_token_pair import CreateTokenPairUseCase
from app.usecases.auth.re_issue_token import ReIssueTokenUseCase
from app.usecases.user.create_or_get_social_user import CreateOrGetSocialUserUseCase

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{provider}/callback", status_code=HTTP_200_OK, response_model=TokenResponse)
async def social_login(
        provider: Provider,
        code: str = Query(..., description="소셜 로그인 인증 코드"),
        social_user_use_case: CreateOrGetSocialUserUseCase = Depends(get_social_user_use_case),
        token_use_case: CreateTokenPairUseCase = Depends(get_create_token_use_case)
):
        from app.infrastructure.auth.social.strategy_resolver import get_social_strategy
        social_user = await get_social_strategy(provider).get_user(code)

        # 2. 사용자 생성 또는 조회
        user = await social_user_use_case.execute(social_user)

        # 3. 토큰 생성
        access_token, refresh_token = await token_use_case.execute(user.id)

        logger.info(f"소셜 로그인 성공: provider={provider}, user_id={user.id}")

        return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.get("/kakao/login", response_class=RedirectResponse)
async def kakao_login():
    """카카오 로그인 페이지로 리다이렉트"""
    kakao_auth_url = (
        f"https://kauth.kakao.com/oauth/authorize"
        f"?client_id={settings.kakao_client_id}"
        f"&redirect_uri={settings.kakao_redirect_uri}"
        f"&response_type=code"
    )

    return RedirectResponse(kakao_auth_url)


@router.post("/token/refresh", response_model=TokenResponse)
async def re_issue_token(
        refresh_token: str = Header(..., alias="X-Refresh-Token", description="리프레시 토큰"),
        use_case: ReIssueTokenUseCase = Depends(get_reissue_token_use_case)
):
    access_token, new_refresh_token = await use_case.execute(refresh_token)

    return TokenResponse(
        access_token=access_token,
        refresh_token=new_refresh_token
    )