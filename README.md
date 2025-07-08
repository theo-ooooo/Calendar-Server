# 🗓️ FastAPI 팀 캘린더 / 일정 공유 API

개인 일정 관리와 팀 단위 일정 공유 기능을 제공하는 FastAPI 기반의 RESTful API입니다.  
JWT 인증, PostgreSQL 연동, 비동기 처리 기반으로 구성되어 있으며, Pytest로 테스트 환경을 갖추고 있습니다.

---

## 📌 기능 요약

- 사용자 인증 (JWT 로그인/회원가입)
- 일정 등록/조회/수정/삭제
- 일정 공유 (특정 유저 또는 팀 단위)
- 반복 일정 (일간/주간/월간)
- 팀 생성 및 팀 멤버 관리
- Swagger 자동 문서화

---

## ⚙️ 기술 스택

| 구성 요소 | 기술 |
|-----------|------|
| 언어 | Python 3.10+ |
| 웹 프레임워크 | FastAPI |
| ORM | SQLAlchemy 2.0 (async) |
| DB | PostgreSQL |
| 마이그레이션 | Alembic |
| 인증 | JWT (OAuth2PasswordBearer) |
| 테스트 | Pytest, HTTPX |
| 문서화 | Swagger UI (자동) |

---

## 🛠️ 프로젝트 구조

```
calendar-api/
├── app/
│   ├── api/v1/         # API 라우터
│   ├── core/           # 설정, 보안 설정
│   ├── db/             # DB 연결, 모델
│   ├── schemas/        # Pydantic 요청/응답 모델
│   ├── services/       # 도메인 로직
│   └── main.py         # FastAPI 진입점
├── tests/              # 테스트 코드
├── alembic/            # DB 마이그레이션
├── .env                # 환경 변수
├── requirements.txt
└── README.md
```

---

## 🚀 실행 방법

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. `.env` 환경 변수 설정
```env
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/calendar
JWT_SECRET_KEY=your_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 3. DB 초기화 (Alembic)
```bash
alembic upgrade head
```

### 4. 서버 실행
```bash
uvicorn app.main:app --reload
```

---

## ✅ 테스트 실행
```bash
pytest
```

---

## 📎 향후 개발 항목

- [ ] 반복 일정 (daily/weekly/monthly)
- [ ] 공유 권한 세분화 (읽기/쓰기/관리)
- [ ] 캘린더 iCal 연동 (.ics)
- [ ] 알림 기능 (Email or 푸시)
- [ ] 관리자 대시보드 (FastAPI-admin or 별도 UI)

---

## 🧑‍💻 개발자

| 이름 | 역할 |
|------|------|
| @theo-ooooo | Backend 개발, API 설계, 구조 설계 |

---
