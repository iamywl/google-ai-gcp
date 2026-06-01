import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Login from './pages/Login';
import Register from './pages/Register';
import ForgotPassword from './pages/ForgotPassword';
import TwoFactorAuth from './pages/TwoFactorAuth';
import Dashboard from './pages/Dashboard';
import Profile from './pages/Profile';
import UserManagement from './pages/UserManagement';
import DepartmentMapping from './pages/DepartmentMapping';
import AuditLogs from './pages/AuditLogs';
import DataUpload from './pages/DataUpload';
import DataConnections from './pages/DataConnections';
import Webhooks from './pages/Webhooks';
import DataScheduler from './pages/DataScheduler';
import FieldMapping from './pages/FieldMapping';
import Preprocessing from './pages/Preprocessing';
import DataMasking from './pages/DataMasking';
import DataExport from './pages/DataExport';
import ProcessDiscovery from './pages/ProcessDiscovery';
import PingPongAnalysis from './pages/PingPongAnalysis';
import Throughput from './pages/Throughput';
import NetworkGraph from './pages/NetworkGraph';
import UploadStandardProcess from './pages/UploadStandardProcess';
import FitnessAnalysis from './pages/FitnessAnalysis';
import ComplianceRisks from './pages/ComplianceRisks';
import BottleneckAnalysis from './pages/BottleneckAnalysis';
import IdleCases from './pages/IdleCases';
import WhatIfSimulation from './pages/WhatIfSimulation';
import AIReports from './pages/AIReports';
import PromptManagement from './pages/PromptManagement';
import SystemMonitoring from './pages/SystemMonitoring';
import AlertSettings from './pages/AlertSettings';

function App() {
  return (
    <BrowserRouter>
      <Routes>
                <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Register />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/2fa" element={<TwoFactorAuth />} />
        
        <Route element={<Layout />}>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/admin/users" element={<UserManagement />} />
        <Route path="/admin/departments" element={<DepartmentMapping />} />
        <Route path="/admin/audit" element={<AuditLogs />} />
        <Route path="/data/upload" element={<DataUpload />} />
        <Route path="/data/connections" element={<DataConnections />} />
        <Route path="/data/webhooks" element={<Webhooks />} />
        <Route path="/data/scheduler" element={<DataScheduler />} />
        <Route path="/data/mapping" element={<FieldMapping />} />
        <Route path="/data/preprocessing" element={<Preprocessing />} />
        <Route path="/data/masking" element={<DataMasking />} />
        <Route path="/data/export" element={<DataExport />} />
        <Route path="/mining/discovery" element={<ProcessDiscovery />} />
        <Route path="/mining/pingpong" element={<PingPongAnalysis />} />
        <Route path="/mining/throughput" element={<Throughput />} />
        <Route path="/mining/network" element={<NetworkGraph />} />
        <Route path="/conformance/standard" element={<UploadStandardProcess />} />
        <Route path="/conformance/fitness" element={<FitnessAnalysis />} />
        <Route path="/conformance/risks" element={<ComplianceRisks />} />
        <Route path="/performance/bottleneck" element={<BottleneckAnalysis />} />
        <Route path="/performance/idle" element={<IdleCases />} />
        <Route path="/performance/simulation" element={<WhatIfSimulation />} />
        <Route path="/ai/reports" element={<AIReports />} />
        <Route path="/ai/prompts" element={<PromptManagement />} />
        <Route path="/settings/system" element={<SystemMonitoring />} />
        <Route path="/settings/alerts" element={<AlertSettings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
