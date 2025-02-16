import React from 'react'
import styles from './LoadingOverlay.module.css'

const LoadingOverlay = ({ loading }) => {
    if (!loading) return null; 
    return (
        <div className={styles.loading_overlay}>
            <div className={styles.spinner}></div>
            <p>잠시만 기다려 주세요...</p>
        </div>
    );
};

export default LoadingOverlay