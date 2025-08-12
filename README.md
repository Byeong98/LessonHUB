# LessonHUB

>  미래 변화에 대응하여 2025년부터 적용되는 2022 개정 교육 과정은 특히 디지털 AI 소양 함양 교육을 강화했다. 
그에 따라  개정된 교육 과정과 디지털 교육자료를 활용하여 수업을 설계해야 하는 교사의 업무와 스트레스를 증가하게 됐다.
> 
> 이를 줄여주기 위해 AI를 활용해 교수안을 작성해주고 그 교수안에 맞는 참고자료를 제공하여 교사들의 편의성을 크 게 높여 주기위해 제작 했습니다.

## 🚀 주요 기능

- 사용자 인증 및 관리
- 교수안 셍성 및 관리
- 참고자료 셍상 및 관리

## 🏗️ 프로젝트 구조

```
lessonHUB/
├── backend/                  # FastAPI 백엔드
│   ├── domain/               # 도메인별 모듈
│   │   ├── users/            # 사용자 관련 기능
│   │   │   ├── crud.py      
│   │   │   ├── router.py    
│   │   │   └── schema.py     
│   │   └── teaches/          
│   │       ├── crud.py      
│   │       ├── router.py     
│   │       └── schema.py     
│   ├── migrations/           
│   ├── teach_data/           # 교육 데이터 파일들
│   ├── main.py               
│   ├── config.py             # 환경 설정
│   ├── database.py           # 데이터베이스 연결
│   ├── models.py             # 데이터베이스 모델
│   ├── auth.py              
│   ├── requirements.txt     
│   └── dockerfile            # 백엔드 Docker 설정
├── frontend/                 # React 프론트엔드
│   ├── src/                 
│   │   ├── components/       
│   │   ├── App.jsx          
│   │   └── index.js        
│   ├── public/             
│   ├── package.json         
│   └── dockerfile            # 프론트엔드 Docker 설정
├── docker-compose.yml        # Docker Compose 설정
└── README.md                 
```

## 📋 설치 및 설정 방법

### 사전 요구사항

- Python 3.13+
- Node.js 16+
- Docker & Docker Compose
- Git

### 1. 백엔드 설정

```bash
cd backend

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일을 편집하여 필요한 환경 변수 설정
```

#### 환경 변수 설정 (.env)

```env
# Backend .env
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
OPENAI_API_KEY=
SQLALCHEMY_ASYNC_DATABASE_URL=
SQLALCHEMY_DATABASE_URL=
HOST=
PORT=
```

```env
# Frontend .env
REACT_APP_BASE_URL=
```

### 2. 프론트엔드 설정

```bash
cd frontend

# 의존성 설치
npm install

# 환경 변수 설정 (필요한 경우)
cp .env.example .env
```

## 🚀 시작 방법

### 개발 환경에서 실행

#### 백엔드 실행

```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate

# 개발 서버 실행
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

백엔드는 `http://localhost:8000`에서 실행됩니다.

- Swagger UI: `http://localhost:8000/docs`

#### 프론트엔드 실행

```bash
cd frontend

# 개발 서버 실행
npm start
```

프론트엔드는 `http://localhost:3000`에서 실행됩니다.

### Docker를 사용한 실행

```bash
# 전체 애플리케이션 실행
docker-compose up -d

# 중지
docker-compose down
```

## 🔧 기술 스택

### 백엔드
- **Framework**: FastAPI
- **Database**: SQLite (개발)
- **ORM**: SQLAlchemy
- **Authentication**: JWT
- **AI Integration**: OpenAI API

### 프론트엔드
- **Framework**: React 19

### 인프라
- **Containerization**: Docker
- **Orchestration**: Docker Compose
