import React, { useState, useContext } from 'react'
import styles from './Login.module.css'
import { useNavigate } from 'react-router-dom';

import Border from '../Border/Border'
import Button from '../Button/Button'
import InputTitle from '../InputTitle/InputTitle'
import { AuthContext } from '../../AuthProvider'
import api from '../../Api';


const InputContainer = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });
  const { username, password } = formData;
  const { setAccessToken, setUserEmail } = useContext(AuthContext);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const validate_data = () => {
    if (!username) {
      alert('아이디를 입력하세요.');
      return false;
    }
    if (!password) {
      alert('비밀번호를 입력하세요.');
      return false;
    }
    return true;
  }

  const handleLogin = async () => {
    if (!validate_data()) return;
    try {
      const response = await api.post(
        "/api/user/login/",
        formData,
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded"
          }
        }
      )
      // 토큰, 이메일 storage에 저장
      Object.entries(response.data).forEach(([key, value]) => {
        localStorage.setItem(key, value);
      });
      setAccessToken(response.data.access_token);
      setUserEmail(response.data.email);

      navigate("/");
      setTimeout(() => {
        window.location.reload(); // 강제 새로고침
      }, 100);
    } catch (error) {
      alert(error.response.data.detail)
    }
  };

  return (
    <div className={styles.input_Container}>
      <h2 className={styles.h2}>로그인</h2>
      <InputTitle
        name='username'
        title='E-mail'
        type='email'
        value={username}
        handleChange={handleChange} />
      <InputTitle
        name='password'
        title='Password'
        type='password'
        value={password}
        handleChange={handleChange} />
      <Button
        width="100%"
        color='black'
        onClick={handleLogin}
      >
        로그인
      </Button>
    </div>
  )
}
const Login = () => {

  return (
    <div className={styles.container}>
      <Border sty='login' bgColor="white" >
        <InputContainer />
      </Border>
    </div>
  )
}

export default Login