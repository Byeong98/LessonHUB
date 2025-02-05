import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import TeachList from './components/TeachList/TeachList'
import TeachCreate from './components/TeachCreate/TeachCreate'
import TeachDetail from './components/TeachDetail/TeachDetail'
import Login from './components/Login/Login'
import NavBar from './components/NavBar/NavBar'
import SignUp from './components/SignUp/SignUp'

function App() {
  return (
    <Router>
      <NavBar />
      <div className="routes_container">
        <Routes >
          <Route path="/" element={<TeachList />} />
          <Route path="/teach/create" element={<TeachCreate />} />
          <Route path="/teach/detail/:id" element={<TeachDetail />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
