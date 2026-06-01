import React from 'react';
import { Link } from 'react-router-dom';

export default function Login() {
  return (
    <div className="auth-container">
      <div className="auth-card">
        <h2>로그인 (Login)</h2>
        <p style={marginBottom: '1.5rem', color: '#64748b'}>FlowLens AI 시스템</p>
        <div className="input-group">
          <label>Email</label>
          <input type="email" placeholder="회사 이메일" />
        </div>
        <div className="input-group">
          <label>Password</label>
          <input type="password" placeholder="비밀번호" />
        </div>
        <Link to="/dashboard"><button className="btn">확인 (Demo Bypass)</button></Link>
        <div style={marginTop: '1rem', textAlign: 'center', fontSize: '0.85rem'}>
          <Link to="/signup" style={marginRight: '1rem'}>회원가입</Link>
          <Link to="/forgot-password">비밀번호 찾기</Link>
        </div>
      </div>
    </div>
  );
}
