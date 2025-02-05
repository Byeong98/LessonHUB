import React from "react";
import styles from "./Button.module.css"; 

const Button = ({ width = "80px", color = "blue", onClick, children }) => {
    return (
        <button 
            className={`${styles.button} ${styles[color]}`} 
            onClick={onClick}
            style={{ width: width }}
        >
            {children}  {/* 버튼 내부 텍스트 or 아이콘 */}
        </button>
    );
};

export default Button;
