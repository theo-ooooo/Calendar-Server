
from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import RedirectResponse
from starlette.status import HTTP_200_OK


from app.domain.auth.provider_type import Provider
from app.infrastructure.auth.jwt_token_service import JwtTokenService
from app.infrastructure.auth.strategy_resolver import get_social_strategy
from app.infrastructure.config import settings
from app.infrastructure.db.database import get_session
from app.infrastructure.user.repository_impl import UserRepositoryImpl
from app.usecases.auth.create_token_pair import CreateTokenPairUseCase
from app.usecases.user.create_or_get_social_user import CreateOrGetSocialUserUseCase

router = APIRouter()

@router.get("/{provider}/callback", status_code=HTTP_200_OK)
async def social_login(
        provider: Provider,
        code:str = Query(...),
        session: AsyncSession = Depends(get_session)):
 social_user = await get_social_strategy(provider).get_user(code)
 social_use_case = CreateOrGetSocialUserUseCase(UserRepositoryImpl(session))
 user = await social_use_case.execute(social_user)

 token_user_case = CreateTokenPairUseCase(JwtTokenService())
 access_token, refresh_token = token_user_case.execute(user.id)

 return {"accessToken": access_token, "refreshToken": refresh_token}




@router.get("/kakao/login")
async def kakao_login():

    return RedirectResponse(
        f"https://kauth.kakao.com/oauth/authorize"
        f"?client_id={settings.kakao_client_id}"
        f"&redirect_uri={settings.kakao_redirect_uri}"
        f"&response_type=code"
    )