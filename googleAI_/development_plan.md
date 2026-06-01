# 개발 계획서: FlowLens AI (Cross-Dept Process Pathologist)

## 1. 프로젝트 개요
본 프로젝트는 기업 내 부서 간 협업 프로세스에서 발생하는 3대 결함(핑퐁, 일탈, 지연)을 이벤트 로그 데이터 기반으로 자동 진단하고, Vertex AI(Gemini)를 활용하여 전략적 개선 리포트를 생성하는 엔터프라이즈급 분석 플랫폼 구축을 목적으로 함.

## 2. 기술 스택 및 아키텍처 (Technical Stack)
- **Runtime**: Python 3.12 (FastAPI)
- **Data Processing**: Pandas (Vectorized Analysis)
- **AI/LLM**: Vertex AI SDK (Gemini 1.5/2.0 Flash)
- **Database**: Cloud SQL (PostgreSQL - Persistence Layer)
- **DevSecOps**: Docker, Cloud Build, Cloud Run, GitHub Actions

## 3. 상세 개발 마일스톤 (Work Breakdown Structure)

### Phase 1: 요구사항 분석 및 아키텍처 설계 (Week 1 - 2)
- **과업 1.1**: 핑퐁, 일탈, 지연/유휴 결함의 수학적 정의 및 탐지 알고리즘 설계.
- **과업 1.2**: OpenAPI Spec 기반 API 엔드포인트 명세(`functional_spec.md`) 확정.
- **과업 1.3**: Mermaid.js를 이용한 시스템 시퀀스 및 데이터 흐름도(`sequence_diagram.md`) 작성.

### Phase 2: 데이터 모델링 및 환경 구축 (Week 3 - 5)
- **과업 2.1**: 표준 이벤트 로그 스키마(`case_id`, `activity`, `timestamp`, `department_from/to`, `action`) 설계 및 ERD(`erd.md`) 반영.
- **과업 2.2**: 유닛 테스트를 위한 1GB급 합성 로그 데이터 생성기(`generate_dummy_data.py`) 고도화.
- **과업 2.3**: 비루트(Non-root) 사용자 보안 설정이 포함된 멀티 스테이지 Dockerfile 최적화.

### Phase 3: 핵심 분석 엔진 및 MVP 개발 (Week 6 - 8)
- **과업 3.1**: Pandas를 활용한 O(n) 복잡도의 핑퐁 및 병목 구간 탐지 엔진 구현.
- **과업 3.2**: 표준 경로(Standard Path) 대조를 통한 프로세스 일탈(Deviance) 탐지 로직 구현.
- **과업 3.3**: 부서별 리드타임 및 유휴 시간(Idle Time) 통계 산출 모듈 개발.

### Phase 4: AI 리포팅 및 대시보드 통합 (Week 9 - 12)
- **과업 4.1**: 지연 구간 및 일탈 원인 분석을 위한 Vertex AI 프롬프트 엔지니어링 및 재시도 전략(Exponential Backoff) 구현.
- **과업 4.2**: FastAPI 중앙 집중식 예외 핸들러 및 구조화된 로깅(Structured Logging) 시스템 통합.
- **과업 4.3**: 분석 결과 영속성 유지를 위한 Repository 레이어(PostgreSQL 연동) 개발.
- **과업 4.4**: Streamlit 기반 인터랙티브 대시보드 개발 및 시각화(Plotly) 연동.

### Phase 5: 검증, 보안 및 배포 (Week 13 - 15)
- **과업 5.1**: BPI Challenge 공개 데이터셋을 활용한 분석 엔진의 정확도(Precision/Recall) 검증.
- **과업 5.2**: Cloud Build 파이프라인 연동 및 Cloud Run 서버리스 배포 자동화.
- **과업 5.3**: 최종 개발 보고서(`development_report.md`) 및 아티팩트 정리.

## 4. 리스크 관리 및 대응 방안 (Risk Mitigation)
| 리스크 항목 | 영향도 | 대응 전략 |
| :--- | :--- | :--- |
| **데이터 보안** | 높음 | 로그 비식별화 처리 및 GCP IAM 역할 기반 접근 제어(RBAC) 적용 |
| **API 할당량(Quota)** | 중간 | Vertex AI 호출 시 처리량 제한(Rate Limiting) 및 결과 캐싱 적용 |
| **분석 성능 저하** | 낮음 | Pandas 연산을 Polars 또는 Dask로 전환하여 분산 처리 검토 |

## 5. 품질 보증 (Quality Assurance)
- **코드 품질**: PEP 8 준수 및 `mypy`를 이용한 정적 타입 검사 실시.
- **테스트 커버리지**: 비즈니스 로직에 대해 최소 80% 이상의 유닛 테스트 커버리지 확보.
- **CI/CD**: `scripts/run_tests.sh` 통과 시에만 배포 파이프라인 트리거.