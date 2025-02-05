import React, { useState } from 'react'
import styles from './Login.module.css'

import Border from '../Border/Border'
import Button from '../Button/Button'
import InputTitle from '../InputTitle/InputTitle'

const Login = () => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState('');

  const handleChange = (event) => {
    const { name, value } = event.target;

    if (name === 'email') {
      setEmail(value);
    } else if (name === 'password') {
      setPassword(value);
    }
  };

  return (
    <div className={styles.container}>
      <Border style='login' bgColor="white" >
        <div className={styles.input_Container}>
          <h2 className={styles.h2}>로그인</h2>
          <InputTitle
            name='email'
            title='E-mail'
            type='email'
            value={email}
            handleChange={handleChange} />
          <InputTitle
            name='password'
            title='Password'
            type='password'
            value={password}
            handleChange={handleChange} />
          <Button width="100%" color='black'>로그인</Button>
        </div>
      </Border>
    </div>
  )
}

export default Login