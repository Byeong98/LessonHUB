import React, { useContext } from 'react'
import style from './NavBar.module.css'
import { Link, useNavigate } from "react-router-dom";


import Button from '../Button/Button'
import { AuthContext } from '../../AuthProvider';



const LoginContainer = () => {
    return (
        <div className={style.lgin_container}>
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
    }

    return (
        <div className={style.lgin_container}>
            <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
                alt="이미지"
                className={style.prople} />
            <p className={style.userEmail}>{userEmail}</p>
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
        <header className={style.header}>
            <Link to="/" className={style.title_link}>
                <h1 className={style.title} >로고</h1>
            </Link>
            {userEmail ? <LogoutContainer userEmail={userEmail} /> : <LoginContainer />}
        </header>
    )
}

export default NavBar