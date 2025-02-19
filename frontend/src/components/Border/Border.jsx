import React from 'react';
import styles from './Border.module.css';

const Border = ({ sty = "login", bgColor = "white", children }) => {
    return (
        <div className={`${styles.container} ${styles[sty]}`} style={{ backgroundColor: bgColor }}>
            {children}
        </div>
    );
};

export default Border;
