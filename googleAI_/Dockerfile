# Stage 1: Build stage
FROM python:3.11-slim AS builder

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final runtime stage
FROM python:3.11-slim

WORKDIR /app

# 비루트 사용자 생성 및 보안 설정
RUN addgroup --system appuser && adduser --system --group appuser

COPY --from=builder /root/.local /home/appuser/.local
COPY . .

ENV PATH=/home/appuser/.local/bin:$PATH
ENV PORT=8080

USER appuser
EXPOSE 8080

CMD uvicorn main:app --host 0.0.0.0 --port $PORT --proxy-headers