# Base image: Python 3.10 이상 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY pay11ama-for-newbies.py .

# 환경 변수 설정 (Docker 외부의 Ollama 서버 접속)
ENV OLLAMA_HOST=http://host.docker.internal:11434

# Streamlit 실행
CMD ["streamlit", "run", "pay11ama-for-newbies.py", "--server.address=0.0.0.0", "--server.port=8501"]
