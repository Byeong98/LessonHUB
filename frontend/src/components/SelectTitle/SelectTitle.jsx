import { useState } from "react";
import styles from "./SelectTitle.module.css"

function SelectTitle({style = "small", title, options, onChange }) {
    const [selectedValue, setSelectedValue] = useState("");

    const handleChange = (event) => {
        setSelectedValue(event.target.value);
        onChange(event.target.value); // 부모 컴포넌트로 값 전달
    };

    return (
        <div className={`${styles.container} ${styles[style]}`}>
            <label htmlFor="options">{title}</label>
            <select id="options"
                    className={`${styles.select} ${selectedValue && styles.selected }`}
                    value={selectedValue} 
                    onChange={handleChange} >
                <option value="">선택하세요</option>
                {options && options.map((option) => (
                    <option key={option.id} value={option.id}>
                        {option.title}
                    </option>
                ))}
            </select>
        </div>
    );
}

export default SelectTitle;


