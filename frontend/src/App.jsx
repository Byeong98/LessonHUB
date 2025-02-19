import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import TeachList from './components/TeachList/TeachList';
import TeachCreate from './components/TeachCreate/TeachCreate';
import TeachDetail from './components/TeachDetail/TeachDetail';
import TeachUpdate from './components/TeachUpdate/TeachUpdate';
import Login from './components/Login/Login';
import SignUp from './components/SignUp/SignUp';
import NavBar from './components/NavBar/NavBar';

import { AuthProvider } from './AuthProvider';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="routes_container">
        <NavBar />
          <Routes >
            <Route path="/" element={<TeachList />} />
            <Route path="/teach/create" element={<TeachCreate />} />
            <Route path="/teach/detail/:id" element={<TeachDetail />} />
            <Route path="/teach/update/:id" element={<TeachUpdate />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
