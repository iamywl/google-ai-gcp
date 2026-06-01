import os
import json

BASE_DIR = "/Users/ywlee/google-ai-gcp/flowlens_platform"
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
BACKEND_DIR = os.path.join(BASE_DIR, "backend")

def create_dir(path):
    os.makedirs(path, exist_ok=True)

# 1. Setup Directories
create_dir(os.path.join(FRONTEND_DIR, "src", "pages"))
create_dir(os.path.join(FRONTEND_DIR, "src", "components"))
create_dir(os.path.join(BACKEND_DIR, "app", "routers"))

# 2. Define 31 Pages mapping
PAGES = [
    {"name": "Login", "route": "/", "title": "로그인 (Login)", "group": "Auth"},
    {"name": "Register", "route": "/signup", "title": "회원가입 (Register)", "group": "Auth"},
    {"name": "ForgotPassword", "route": "/forgot-password", "title": "비밀번호 찾기 (Forgot Password)", "group": "Auth"},
    {"name": "TwoFactorAuth", "route": "/2fa", "title": "2단계 인증 (2FA)", "group": "Auth"},
    
    {"name": "Dashboard", "route": "/dashboard", "title": "대시보드 (KPI Dashboard)", "group": "Main"},
    
    {"name": "Profile", "route": "/profile", "title": "내 프로필 (Profile)", "group": "User"},
    {"name": "UserManagement", "route": "/admin/users", "title": "사용자 관리 (User Mgmt & RBAC)", "group": "User"},
    {"name": "DepartmentMapping", "route": "/admin/departments", "title": "부서 및 조직도 (Dept Mapping)", "group": "User"},
    {"name": "AuditLogs", "route": "/admin/audit", "title": "감사 로그 (Audit Trail)", "group": "User"},
    
    {"name": "DataUpload", "route": "/data/upload", "title": "데이터 수동 업로드 (CSV/Excel)", "group": "Data Ingestion"},
    {"name": "DataConnections", "route": "/data/connections", "title": "시스템 연동 (ERP/Groupware)", "group": "Data Ingestion"},
    {"name": "Webhooks", "route": "/data/webhooks", "title": "웹훅 설정 (Webhooks)", "group": "Data Ingestion"},
    {"name": "DataScheduler", "route": "/data/scheduler", "title": "수집 스케줄러 (Scheduler)", "group": "Data Ingestion"},
    
    {"name": "FieldMapping", "route": "/data/mapping", "title": "필드 매핑 UI (Field Mapping)", "group": "Data Processing"},
    {"name": "Preprocessing", "route": "/data/preprocessing", "title": "전처리 및 누락값 보정", "group": "Data Processing"},
    {"name": "DataMasking", "route": "/data/masking", "title": "데이터 비식별화 (Masking)", "group": "Data Processing"},
    {"name": "DataExport", "route": "/data/export", "title": "XES 데이터 내보내기", "group": "Data Processing"},
    
    {"name": "ProcessDiscovery", "route": "/mining/discovery", "title": "프로세스 맵 (Process Map)", "group": "Process Mining"},
    {"name": "PingPongAnalysis", "route": "/mining/pingpong", "title": "부서 간 핑퐁 탐지 (Ping-pong)", "group": "Process Mining"},
    {"name": "Throughput", "route": "/mining/throughput", "title": "부서별 처리량 (Throughput)", "group": "Process Mining"},
    {"name": "NetworkGraph", "route": "/mining/network", "title": "협업 네트워크 시각화", "group": "Process Mining"},
    
    {"name": "UploadStandardProcess", "route": "/conformance/standard", "title": "표준 프로세스 업로드", "group": "Conformance"},
    {"name": "FitnessAnalysis", "route": "/conformance/fitness", "title": "적합도 및 일탈 분석", "group": "Conformance"},
    {"name": "ComplianceRisks", "route": "/conformance/risks", "title": "컴플라이언스 위반 리스크", "group": "Conformance"},
    
    {"name": "BottleneckAnalysis", "route": "/performance/bottleneck", "title": "병목 부서 및 대기 시간", "group": "Performance"},
    {"name": "IdleCases", "route": "/performance/idle", "title": "장기 방치 및 유휴 탐지", "group": "Performance"},
    {"name": "WhatIfSimulation", "route": "/performance/simulation", "title": "What-If 시뮬레이션", "group": "Performance"},
    
    {"name": "AIReports", "route": "/ai/reports", "title": "AI 자연어 개선 리포트", "group": "AI Insights"},
    {"name": "PromptManagement", "route": "/ai/prompts", "title": "프롬프트 템플릿 관리", "group": "AI Insights"},
    
    {"name": "SystemMonitoring", "route": "/settings/system", "title": "시스템 리소스 모니터링", "group": "System"},
    {"name": "AlertSettings", "route": "/settings/alerts", "title": "알림 및 SLA 설정", "group": "System"},
]

# 3. Write Frontend configuration
package_json = {
  "name": "flowlens-frontend",
  "private": True,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.22.3"
  },
  "devDependencies": {
    "@types/react": "^18.2.66",
    "@types/react-dom": "^18.2.22",
    "@vitejs/plugin-react": "^4.2.1",
    "typescript": "^5.2.2",
    "vite": "^5.2.0"
  }
}

with open(os.path.join(FRONTEND_DIR, "package.json"), "w") as f:
    json.dump(package_json, f, indent=2)

vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
"""
with open(os.path.join(FRONTEND_DIR, "vite.config.ts"), "w") as f:
    f.write(vite_config)

tsconfig = {
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": True,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": True,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": True,
    "resolveJsonModule": True,
    "isolatedModules": True,
    "noEmit": True,
    "jsx": "react-jsx",
    "strict": True,
    "noUnusedLocals": False,
    "noUnusedParameters": False,
    "noFallthroughCasesInSwitch": True
  },
  "include": ["src"]
}
with open(os.path.join(FRONTEND_DIR, "tsconfig.json"), "w") as f:
    json.dump(tsconfig, f, indent=2)

index_html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>FlowLens AI</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>"""
with open(os.path.join(FRONTEND_DIR, "index.html"), "w") as f:
    f.write(index_html)

# 4. Write Frontend React Source
main_tsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""
with open(os.path.join(FRONTEND_DIR, "src", "main.tsx"), "w") as f:
    f.write(main_tsx)

index_css = """
:root {
  --primary: #2563eb;
  --bg: #f8fafc;
  --text: #0f172a;
  --sidebar-bg: #1e293b;
  --sidebar-text: #cbd5e1;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: var(--bg); color: var(--text); }
.app-container { display: flex; height: 100vh; overflow: hidden; }
.sidebar { width: 250px; background-color: var(--sidebar-bg); color: var(--sidebar-text); padding: 1rem 0; overflow-y: auto; }
.sidebar h2 { padding: 0 1.5rem; margin-bottom: 1rem; color: white; font-size: 1.2rem;}
.sidebar-group { margin-bottom: 1rem; }
.sidebar-group-title { font-size: 0.8rem; text-transform: uppercase; padding: 0 1.5rem; margin-bottom: 0.5rem; color: #94a3b8; }
.sidebar a { display: block; padding: 0.5rem 1.5rem; color: var(--sidebar-text); text-decoration: none; font-size: 0.9rem; }
.sidebar a:hover { background-color: #334155; color: white; }
.main-content { flex: 1; padding: 2rem; overflow-y: auto; }
.card { background: white; border-radius: 8px; padding: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); margin-bottom: 1.5rem; }
.card h3 { margin-bottom: 1rem; color: #1e293b; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
.placeholder-box { background: #f1f5f9; height: 200px; border-radius: 4px; display: flex; align-items: center; justify-content: center; color: #64748b; border: 1px dashed #cbd5e1; }
.auth-container { display: flex; height: 100vh; align-items: center; justify-content: center; background: #e2e8f0; }
.auth-card { background: white; padding: 2.5rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 400px; }
.input-group { margin-bottom: 1rem; }
.input-group label { display: block; margin-bottom: 0.5rem; font-size: 0.9rem; }
.input-group input { width: 100%; padding: 0.5rem; border: 1px solid #cbd5e1; border-radius: 4px; }
.btn { width: 100%; padding: 0.75rem; background: var(--primary); color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 1rem; }
.btn:hover { background: #1d4ed8; }
"""
with open(os.path.join(FRONTEND_DIR, "src", "index.css"), "w") as f:
    f.write(index_css)

# Generate Pages
imports = []
routes = []

for page in PAGES:
    name = page['name']
    route = page['route']
    title = page['title']
    
    # Write Component
    is_auth = page['group'] == "Auth"
    
    if is_auth:
        comp_code = f"""import React from 'react';
import {{ Link }} from 'react-router-dom';

export default function {name}() {{
  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2>{title}</h2>
        <p style={{marginBottom: '1.5rem', color: '#64748b'}}>FlowLens AI 시스템</p>
        <div className="input-group">
          <label>Email</label>
          <input type="email" placeholder="회사 이메일" />
        </div>
        <div className="input-group">
          <label>Password</label>
          <input type="password" placeholder="비밀번호" />
        </div>
        <Link to="/dashboard"><button className="btn">확인 (Demo Bypass)</button></Link>
        <div style={{marginTop: '1rem', textAlign: 'center', fontSize: '0.85rem'}}>
          <Link to="/signup" style={{marginRight: '1rem'}}>회원가입</Link>
          <Link to="/forgot-password">비밀번호 찾기</Link>
        </div>
      </div>
    </div>
  );
}}
"""
    else:
        comp_code = f"""import React from 'react';

export default function {name}() {{
  return (
    <div>
      <h1 style={{marginBottom: '1.5rem'}}>{title}</h1>
      <p style={{marginBottom: '2rem', color: '#64748b'}}>이 화면은 117개의 기능 명세 중 '{title}' 모듈을 구현한 뷰입니다.</p>
      
      <div className="grid">
        <div className="card">
          <h3>상세 데이터 조회</h3>
          <div className="placeholder-box">데이터 테이블 / 그리드 뷰 영역</div>
        </div>
        <div className="card">
          <h3>분석 및 시각화</h3>
          <div className="placeholder-box">D3.js / React Flow 차트 영역</div>
        </div>
      </div>
      
      <div className="card">
        <h3>AI 리포트 요약</h3>
        <p style={{lineHeight: 1.6, color: '#334155'}}>해당 기능에 대한 AI의 분석 결과가 여기에 표시됩니다. 프로세스 병목이나 위험 요소를 식별하여 자연어로 설명합니다.</p>
      </div>
    </div>
  );
}}
"""
    
    with open(os.path.join(FRONTEND_DIR, "src", "pages", f"{name}.tsx"), "w") as f:
        f.write(comp_code)
        
    imports.append(f"import {name} from './pages/{name}';")
    routes.append(f'        <Route path="{route}" element={{<{name} />}} />')


# Write Layout
sidebar_links = ""
groups = {}
for p in PAGES:
    if p['group'] != "Auth":
        if p['group'] not in groups:
            groups[p['group']] = []
        groups[p['group']].append(p)

for group, items in groups.items():
    sidebar_links += f'        <div className="sidebar-group">\n'
    sidebar_links += f'          <div className="sidebar-group-title">{group}</div>\n'
    for p in items:
        sidebar_links += f'          <Link to="{p["route"]}">{p["title"].split(" (")[0]}</Link>\n'
    sidebar_links += f'        </div>\n'


layout_tsx = f"""import React from 'react';
import {{ Link, Outlet }} from 'react-router-dom';

export default function Layout() {{
  return (
    <div className="app-container">
      <div className="sidebar">
        <h2>FlowLens AI</h2>
{sidebar_links}
      </div>
      <div className="main-content">
        <Outlet />
      </div>
    </div>
  );
}}
"""
with open(os.path.join(FRONTEND_DIR, "src", "components", "Layout.tsx"), "w") as f:
    f.write(layout_tsx)


# Write App.tsx
app_tsx = f"""import React from 'react';
import {{ BrowserRouter, Routes, Route }} from 'react-router-dom';
import Layout from './components/Layout';
{chr(10).join(imports)}

function App() {{
  return (
    <BrowserRouter>
      <Routes>
        {chr(10).join([r for r, p in zip(routes, PAGES) if p['group'] == 'Auth'])}
        
        <Route element={{<Layout />}}>
{chr(10).join([r for r, p in zip(routes, PAGES) if p['group'] != 'Auth'])}
        </Route>
      </Routes>
    </BrowserRouter>
  );
}}

export default App;
"""
with open(os.path.join(FRONTEND_DIR, "src", "App.tsx"), "w") as f:
    f.write(app_tsx)


# 5. Write Backend Shell
backend_main = """from fastapi import FastAPI

app = FastAPI(title="FlowLens AI Backend", description="API for Process Mining & AI Reports")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FlowLens AI API Server is running"}

# Mock endpoints covering 10 modules
@app.get("/api/v1/health")
def health_check():
    return {"status": "healthy", "modules": 10, "features": 117}

@app.post("/api/v1/auth/login")
def login(): pass

@app.get("/api/v1/mining/pingpong")
def get_pingpong_data():
    return {"data": [{"dept": "구매팀", "bounce": 14, "risk": "High"}]}
    
@app.get("/api/v1/ai/report")
def generate_report():
    return {"report": "구매팀과 재무팀 간의 반려가 14회 발생하여 전체 지연의 30%를 차지합니다."}
"""
with open(os.path.join(BACKEND_DIR, "app", "main.py"), "w") as f:
    f.write(backend_main)
    
req_txt = "fastapi\nuvicorn\npydantic\n"
with open(os.path.join(BACKEND_DIR, "requirements.txt"), "w") as f:
    f.write(req_txt)

print("FlowLens AI Platform App has been successfully generated.")
