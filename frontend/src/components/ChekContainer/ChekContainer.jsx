import { useState } from "react";
import styles from "./ChekContainer.module.css";
import Border from "../Border/Border";

const CheckboxTitle = ({ options, onChange }) => {
  const [selectedValues, setSelectedValues] = useState([]);

  const handleCheckChange = (event, value) => {
    const newSelectedValues = event.target.checked
      ? [...selectedValues, value] 
      : selectedValues.filter((val) => val !== value); 

    setSelectedValues(newSelectedValues);

    if (onChange) {
      onChange(newSelectedValues); // 부모 컴포넌트로 값 전달
    }
  };

  return (
    <div className={styles.container}>
      {options.map((option, index) => (
        <label key={index} className={styles.checkbox_label}>
          <input
            type="checkbox"
            name="checkbox"
            checked={selectedValues.includes(option.value)} 
            onChange={(event) => handleCheckChange(event, option.value)} // 상태 업데이트 후 부모로 값 전달
          />
          <span>{option.label}</span>
        </label>
      ))}
    </div>
  );
};

const ChekContainer = ({ style = "checkbox", title, optionsList, onChange }) => {
  return (
    <div className={styles.checkbox_container}>
      <p>{title}</p>
      <Border style={style} bgColor="rgba(245,245,245,1)">
        <CheckboxTitle options={optionsList} onChange={onChange} />
      </Border>
    </div>
  );
};

export default ChekContainer;
