import React, { useContext } from 'react'
import styles from './NavBar.module.css'
import { Link, useNavigate } from "react-router-dom";


import Button from '../Button/Button'
import { AuthContext } from '../../AuthProvider';



const LoginContainer = () => {
    return (
        <div className={styles.lgin_container}>
            <Link to="/login">
                <Button width='100px' color='gray'>로그인</Button>
            </Link>
            <Link to="/signup">
                <Button width='100px' color='black'>회원가입</Button>
            </Link>
        </div>
    )
}

const LogoutContainer = ({ userEmail }) => {
    const { setAccessToken, setUserEmail } = useContext(AuthContext);
    const navigate = useNavigate();
    const handelLogout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('token_type');
        localStorage.removeItem('email');
        setAccessToken(null);
        setUserEmail(null);
        navigate("/");
        setTimeout(() => {
            window.location.reload(); // 강제 새로고침
        }, 100);
    };

    return (
        <div className={styles.lgin_container}>
            <img src="/blank-profile.webp"
                alt="이미지"
                className={styles.prople} />
            <p className={styles.userEmail}>{userEmail}</p>
            <Button
                width='100px'
                color='black'
                onClick={handelLogout}
            >
                로그아웃
            </Button>
        </div>
    )
}


const NavBar = () => {
    const { userEmail } = useContext(AuthContext);
    return (
        <header className={styles.header}>
            <Link to="/" className={styles.title_link}>
                <img src="/lessonhub-removebg.png" alt="lessonhub" className={styles.logo} />
            </Link>
            {userEmail ? <LogoutContainer userEmail={userEmail} /> : <LoginContainer />}
        </header>
    )
}

export default NavBar