import React, { useState } from 'react'
import styles from './SignUp.module.css'
import { useNavigate } from 'react-router-dom';

import Border from '../Border/Border'
import Button from '../Button/Button'
import InputTitle from '../InputTitle/InputTitle'
import axios from "axios";

const InputContainer = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        email: '',
        password1: '',
        password2: '',
    });
    const { email, password1, password2 } = formData;

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handlSignUP = async () => {
        try {
            const response = await axios.post(
                "http://127.0.0.1:8000/api/user/create",
                formData,
                {
                    headers: {
                        "Content-Type": "application/json",
                    }
                }
            )
            alert('회원가입 성공');
            navigate('/');
        } catch (error) {
            if (error.response && error.response.data) {
                const errorStatus = error.response.status;
                const errorDetail = error.response.data.detail;

                if (errorStatus === 422) {
                    alert(errorDetail[0].msg.replace(/^.*?,\s*/, '', ''));
                } else if (errorStatus === 409) {
                    alert(errorDetail);
                } 
            } else {
                alert('서버 연결 실패');
            }
        }
    }

    return (
        <div className={styles.input_Container}>
            <h2 className={styles.h2}>회원가입</h2>
            <InputTitle
                name='email'
                title='E-mail'
                type='email'
                value={email}
                handleChange={handleChange} />
            <InputTitle
                name='password1'
                title='Password1'
                type='password'
                value={password1}
                handleChange={handleChange} />
            <InputTitle
                name='password2'
                title='Confirm Password'
                type='password'
                value={password2}
                handleChange={handleChange} />
            <Button
                width="100%"
                color='black'
                onClick={handlSignUP}
            >
                회원가입
            </Button>
        </div>
    )
}


const SignUp = () => {
    return (
        <div className={styles.container}>
            <Border style='signup' bgColor="white" >
                <InputContainer />
            </Border>
        </div>
    )
}

export default SignUp