import { useState, useEffect } from "react";
import styles from "./ChekContainer.module.css";
import Border from "../Border/Border";

const CheckboxTitle = ({ options, onChange, allowDuplicates, selectedValues, setSelectedValues }) => {

  const handleCheckChange = (event, id) => {
    const isChecked = event.target.checked;
    let updatedValues;

    if (allowDuplicates) {
      updatedValues = isChecked
        ? [...selectedValues, id] 
        : selectedValues.filter((value) => value !== id); 
    } else {
      // 단일 선택일 경우 값 하나만 저장
      updatedValues = isChecked ? id : null;
    }

    setSelectedValues(updatedValues);
    onChange(updatedValues);
  };
  return (
    <div className={styles.container}>
      {options &&
        options.map((option, index) => (
          <label key={index} className={styles.checkbox_label}>
            <input
              type="checkbox"
              name="checkbox"
              checked={allowDuplicates ? selectedValues.includes(option.id) : selectedValues === option.id}
              onChange={(event) => handleCheckChange(event, option.id)}
            />
            <span>{option.title}</span>
          </label>
        ))}
    </div>
  );
};

const ChekContainer = ({ sty = "checkbox", title, optionsList, onChange, allowDuplicates = true, selectedIds }) => {
  const [selectedValues, setSelectedValues] = useState(selectedIds || []);

  // formData.standard_id가 변경되면 selectedValues도 업데이트
  useEffect(() => {
    setSelectedValues(selectedIds || []);
  }, [selectedIds]);

  return (
    <div className={styles.checkbox_container}>
      <p>{title}</p>
      <Border sty={sty} bgColor="rgba(245,245,245,1)">
        <CheckboxTitle 
        options={optionsList} 
        onChange={onChange} 
        allowDuplicates={allowDuplicates}
        selectedValues={selectedValues}
        setSelectedValues={setSelectedValues} />
      </Border>
    </div>
  );
};

export default ChekContainer;
