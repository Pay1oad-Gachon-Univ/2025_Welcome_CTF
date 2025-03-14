FROM python:3.9-slim@sha256:d1fd807555208707ec95b284afd10048d0737e84b5f2d6fdcbed2922b9284b56

# socat 설치 (네트워크 연결을 prob.py로 포워딩)
RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

# 보안을 위해 비루트 사용자 생성
RUN adduser --disabled-password --gecos '' ctf

WORKDIR /home/ctf

# prob.py와 flag 파일을 컨테이너에 복사
COPY prob.py .
COPY flag .

# 파일 소유권을 ctf 사용자로 변경
RUN chown -R ctf:ctf /home/ctf

USER ctf

# 컨테이너가 열 포트 (예: 9004) 노출
EXPOSE 9999

# socat을 이용해 TCP 포트 9004에서 연결을 받고, 연결 시 python prob.py를 실행
CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:python prob.py"]
