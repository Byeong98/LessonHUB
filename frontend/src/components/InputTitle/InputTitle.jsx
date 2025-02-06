import React, { useId } from 'react'
import styles from './InputTitle.module.css'

const InputTitle = ({ name, height = "40px", title = "title", type = 'text', value = '', handleChange }) => {
    const id = useId();

    return (
        <div className={styles.inputField}>
            <label htmlFor={id} className={styles.label}>
                {title}
            </label>
            <input
                id={id}
                name={name}
                type={type}
                value={value}
                placeholder={`${title}`}
                onChange={handleChange}
                className={styles.input}
                style={{ height: height }}
            />
        </div>
    )
}

export default InputTitle