#!/bin/bash

# 1. 더미 데이터 생성
python3 /home/yoonwoodev/plan_A/scripts/generate_dummy_data.py

# 2. 로컬 테스트 (서버가 떠있다고 가정하거나 CI 단계에서 실행)
echo "Running Integration Test..."

RESPONSE=$(curl -s -X POST "http://localhost:8080/v1/analyze" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/home/yoonwoodev/plan_A/dummy_logs.csv")

if [[ $RESPONSE == *"ai_report"* ]]; then
  echo "Validation Success: AI Report generated."
else
  echo "Validation Failed: AI Report missing."
  exit 1
fi
