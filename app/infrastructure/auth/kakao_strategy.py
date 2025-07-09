
import httpx

from app.api.v1.auth.schema import LoginRequest
from app.domain.auth.social_strategy import SocialLoginStrategy
from app.domain.user.social_user import SocialUser
from app.infrastructure.config import settings


class KakaoAuthStrategy(SocialLoginStrategy):
    async def get_user(self, code: str) -> SocialUser:
        async with httpx.AsyncClient() as client:
            token_response = await client.post("https://kauth.kakao.com/oauth/token", data={
                "grant_type": "authorization_code",
                "client_id": settings.kakao_client_id,
                "redirect_uri": settings.kakao_redirect_uri,
                "code": code,
            })

            res_json = token_response.json()

            if not res_json.get("access_token"):
                print("res", res_json)
                from fastapi import HTTPException
                raise HTTPException(status_code=400, detail="Kakao login failed")

            access_token = res_json["access_token"]

            user_response = await client.get(
                "https://kapi.kakao.com/v2/user/me",
                headers={"Authorization": f"Bearer {access_token}"}
            )

            data = user_response.json()
            account = data["kakao_account"]
            profile = account.get("profile", {})

            return SocialUser(
                uid=str(data["id"]),
                provider="kakao",
                email=account.get("email"),
                nickname=profile.get("nickname")
            )
