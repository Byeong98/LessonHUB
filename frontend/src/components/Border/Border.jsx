import React from 'react';
import styles from './Border.module.css';

const Border = ({ style = "login", bgColor = "white", children }) => {
    return (
        <div className={`${styles.container} ${styles[style]}`} style={{ backgroundColor: bgColor }}>
            {children}
        </div>
    );
};

export default Border;
