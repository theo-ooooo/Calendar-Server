from typing import Optional, Any


class ApiResponse:

    @staticmethod
    def success(message: str = "요청이 성공적으로 처리되었습니다.", data: Optional[Any] = None, status_code:int = 200, **kwargs) -> dict:
        response :dict = {
            "status": "success",
            "message": message,
            **kwargs
        }

        if data is not None:
            response["data"] = data

        return response

    @staticmethod
    def created(
            message: str = "리소스가 성공적으로 생성되었습니다.",
            data: Optional[Any] = None,
            status_code:int = 201,
            **kwargs
    ) -> dict:
        return ApiResponse.success(
            message=message,
            data=data,
            status_code=status_code,
            **kwargs
        )

    @staticmethod
    def no_content(message: str = "요청이 성공적으로 처리되었습니다.") -> dict:
        """내용 없음 응답 (204)"""
        return {
            "status": "success",
            "message": message
        }