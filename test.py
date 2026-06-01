from google import genai

# google-genai SDK 1.0+ 공식 규격
# vertexai=True 플래그를 통해 GCP 프로젝트 인프라 및 결제 라인과 연동됩니다.
client = genai.Client(
    vertexai=True,
    project="knudc-yoonwoodev",
    location="us-central1"
)

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Cloud Shell 인프라를 통한 Vertex AI 최종 호출 검증입니다.',
)

print(response.text)
