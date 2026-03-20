# nongameanbun - mainAction

## 프로젝트 구조
```text
.
├── main.py # 메인 액션 서버 실행 엔트리포인트 및 API 라우터
├── gateway.py # 외부 서비스 연동을 위한 게이트웨이
├── runner.py # 메인 액션 실행 및 테스트 스크립트
├── test.ipynb # 테스트 및 실험용 노트북
├── env.example # 환경 변수 예시 파일
├── build # 빌드별 동작 모듈 (AbstractBuild, FinalBuild, Adele, Len, Shadower, Zero 등)
└── utils # 위치, 예외 처리 등 모듈 내 공통 사용 유틸리티 
```

## 사전 요구 사항

### 환경 변수 세팅 (`.env`)
환경에 맞게 각 포트 번호를 지정하여 프로젝트 루트에 `.env` 파일을 생성합니다.

```powershell
Copy-Item env.example .env
```

`env.example` 포맷 예시:
```ini
RUNE_SOLVER_PORT=8020
inputHandler_API_PORT=8001
statusChecker_API_PORT=8002
alarmHandler_API_PORT=8003
intrAction_API_PORT=8004
mainAction_API_PORT=8005
subaction_API_PORT=8006
streaning_API_PORT=8007
objectDetector_API_PORT=8008
agentServer_API_PORT=8009
```

## 실행 방법

```bash
pip install -r requirements.txt
python main.py
```

`localhost:8005/docs` 로 swagger 명세를 확인 가능
