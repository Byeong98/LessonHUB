import React from 'react'
import style from './NavBar.module.css'
import { Link } from "react-router-dom";

import Button from '../Button/Button'


const NavBar = () => {


    return (
        <heder className={style.heder}>
            <Link to="/" className={style.title_link}>
                <h1 className={style.title} >로고</h1>
            </Link>
            <div className={style.lgin_container}>
                <Link to="/login">
                    <Button width='100px' color='gray'>로그인</Button>
                </Link>
                <Link to="/signup">
                    <Button width='100px' color='gray'>회원가입</Button>
                </Link>
            </div>
        </heder>
    )
}

export default NavBar