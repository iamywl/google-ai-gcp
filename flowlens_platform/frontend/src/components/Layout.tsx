import React from 'react';
import { Link, Outlet } from 'react-router-dom';

export default function Layout() {
  return (
    <div className="app-container">
      <div className="sidebar">
        <h2>FlowLens AI</h2>
        <div className="sidebar-group">
          <div className="sidebar-group-title">Main</div>
          <Link to="/dashboard">대시보드</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">User</div>
          <Link to="/profile">내 프로필</Link>
          <Link to="/admin/users">사용자 관리</Link>
          <Link to="/admin/departments">부서 및 조직도</Link>
          <Link to="/admin/audit">감사 로그</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">Data Ingestion</div>
          <Link to="/data/upload">데이터 수동 업로드</Link>
          <Link to="/data/connections">시스템 연동</Link>
          <Link to="/data/webhooks">웹훅 설정</Link>
          <Link to="/data/scheduler">수집 스케줄러</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">Data Processing</div>
          <Link to="/data/mapping">필드 매핑 UI</Link>
          <Link to="/data/preprocessing">전처리 및 누락값 보정</Link>
          <Link to="/data/masking">데이터 비식별화</Link>
          <Link to="/data/export">XES 데이터 내보내기</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">Process Mining</div>
          <Link to="/mining/discovery">프로세스 맵</Link>
          <Link to="/mining/pingpong">부서 간 핑퐁 탐지</Link>
          <Link to="/mining/throughput">부서별 처리량</Link>
          <Link to="/mining/network">협업 네트워크 시각화</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">Conformance</div>
          <Link to="/conformance/standard">표준 프로세스 업로드</Link>
          <Link to="/conformance/fitness">적합도 및 일탈 분석</Link>
          <Link to="/conformance/risks">컴플라이언스 위반 리스크</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">Performance</div>
          <Link to="/performance/bottleneck">병목 부서 및 대기 시간</Link>
          <Link to="/performance/idle">장기 방치 및 유휴 탐지</Link>
          <Link to="/performance/simulation">What-If 시뮬레이션</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">AI Insights</div>
          <Link to="/ai/reports">AI 자연어 개선 리포트</Link>
          <Link to="/ai/prompts">프롬프트 템플릿 관리</Link>
        </div>
        <div className="sidebar-group">
          <div className="sidebar-group-title">System</div>
          <Link to="/settings/system">시스템 리소스 모니터링</Link>
          <Link to="/settings/alerts">알림 및 SLA 설정</Link>
        </div>

      </div>
      <div className="main-content">
        <Outlet />
      </div>
    </div>
  );
}
