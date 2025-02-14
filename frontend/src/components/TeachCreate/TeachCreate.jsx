import React, { useState } from 'react'
import styles from './TeachCreate.module.css'

import Border from '../Border/Border'
import Button from '../Button/Button'
import SelectTitle from '../SelectTitle/SelectTitle'
import ChekContainer from '../ChekContainer/ChekContainer'

const SelectContainer = () => {
  const [selectedOption, setSelectedOption] = useState("");

  const optionsList = [
    { value: "math", label: "수학" },
    { value: "science", label: "과학" },
    { value: "korean", label: "국어" },
  ];

  return (
    <div className={styles.select_container} >
      <SelectTitle title="학년" options={optionsList} onChange={setSelectedOption} />
      <SelectTitle title="과목" options={optionsList} onChange={setSelectedOption} />
      <SelectTitle title="과목상세" options={optionsList} onChange={setSelectedOption} />
    </div>
  )
}

const ButtonContainer = () => {
  return (
    <div className={styles.button_container}>
      <Button
        width="45%"
        color='black'
        onClick=""
      >
        확인
      </Button>
      <Button
        width="45%"
        onClick=""
      >
        취소
      </Button>
    </div>
  )
}

const TeachCreate = () => {
  const [checkedValues, setCheckedValues] = useState([]);

  // 자식 컴포넌트에서 전달된 값으로 상태 업데이트
  const handleCheckboxChange = (selectedValues) => {
    setCheckedValues(selectedValues); // 부모 상태 업데이트
  };

  const optionsList = [
    { value: "math", label: "수학" },
    { value: "science", label: "과학" },
    { value: "korean", label: "국어" },
    { value: "math", label: "수학" },
    { value: "science", label: "과학" },
    { value: "korean", label: "국어" },
    { value: "math", label: "수학" },
    { value: "science", label: "과학" },
    { value: "korean", label: "국어" },
    { value: "math", label: "수학" },
    { value: "science", label: "과학" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "math", label: "수학" },
    { value: "science", label: "과학" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "math", label: "수학" },
    { value: "science", label: "과학" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    { value: "korean", label: "국어" },
    // 다른 항목들
  ];


  return (
    <div className={styles.container}>
      <Border style='TeachingForm' bgColor="white" >
        <div className={styles.content_container}>
          <h3>교수안 생성</h3>
          <SelectContainer />
          <ChekContainer title="단원" optionsList={optionsList} onChange={handleCheckboxChange} />
          <ChekContainer style = "checkbox_large" title="성취기준" optionsList={optionsList} onChange={handleCheckboxChange} />
          <ButtonContainer />
        </div>
      </Border>
    </div>
  )
}

export default TeachCreate