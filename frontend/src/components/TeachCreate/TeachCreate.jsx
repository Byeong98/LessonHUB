import React, { useState, useEffect, useContext } from 'react';
import styles from './TeachCreate.module.css';
import { useNavigate } from 'react-router-dom';

import Border from '../Border/Border';
import Button from '../Button/Button';
import SelectTitle from '../SelectTitle/SelectTitle';
import ChekContainer from '../ChekContainer/ChekContainer';
import LoadingOverlay from '../LoadingOverlay/LoadingOverlay';

import { AuthContext } from '../../AuthProvider';
import api from "../../api";

const SelectContainer = ({ data, onChange }) => {
  return (
    <div className={styles.select_container} >
      <SelectTitle title="학년" options={data.grades} onChange={(value) => onChange("grade_id", value)} />
      <SelectTitle title="과목" options={data.subjects} onChange={(value) => onChange("subject_id", value)} />
      <SelectTitle title="과목상세" options={data.sections} onChange={(value) => onChange("section_id", value)} />
    </div>
  )
}

const ButtonContainer = ({ formData, setLoading }) => {
  const navigate = useNavigate();
  const { accessToken } = useContext(AuthContext);

  const handlTeachCreate = async () => {
    if (!accessToken) return;

    setLoading(true);
    try {
      const response = await api.post(
        "/api/teach/create/",
        formData,
        {
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${accessToken}`,
          }
        }
      )
      navigate(`/teach/detail/${response.data.id}`);
    } catch (error) {
      alert('서버 연결 실패');
    }
    setLoading(false);
  }

return (
  <div className={styles.button_container}>
    <Button
      width="45%"
      color='black'
      onClick={handlTeachCreate}
    >
      확인
    </Button>
    <Button
      width="45%"
      onClick={() => navigate("/")}
    >
      취소
    </Button>
  </div>
)
}

const TeachCreate = () => {
  const [loading, setLoading] = useState(false); 
  const [formData, setFormData] = useState({
    grade_id: "",
    subject_id: "",
    section_id: "",
    unit_id: "",
    standard_id: []
  });
  const [data, setData] = useState({
    grades: [],
    subjects: [],
    sections: [],
    units: [],
    standards: []
  });

  // 학년 + 과목 데이터 가져오기
  useEffect(() => {
    Promise.all([
      api.get("/api/teach/grades/"),
      api.get("/api/teach/subjects/")
    ])
      .then(([gradesRes, subjectsRes]) => {
        setData({
          grades: gradesRes.data,
          subjects: subjectsRes.data
        });
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, []);


  const handleSelectChange = (key, value) => {
    setFormData(prev => ({
      ...prev,
      [key]: value, // 선택한 값을 업데이트
    }));
  };

  // 과목 상세 가져오기
  useEffect(() => {
    if (!formData.subject_id) return;

    setData(prev => ({
      ...prev,
      sections: [],
      units: [],
      standards: []
    }));

    api.get(`api/teach/${Number(formData.subject_id)}/sections/`)
      .then(response => setData(prev => ({
        ...prev,
        sections: response.data,
      })))
      .catch((error) => console.error("Error fetching data:", error));
  }, [formData.subject_id]);

  // 단원 가져오기
  useEffect(() => {
    if (!formData.section_id) return;

    setData(prev => ({
      ...prev,
      units: [],
      standards: []
    }));

    api.get(`api/teach/${Number(formData.section_id)}/units/`)
      .then(response => setData(prev => ({
        ...prev,
        units: response.data,
      })))
      .catch((error) => console.error("Error Unuts:", error));
  }, [formData.section_id]);

  // 성취 기준  가져오기
  useEffect(() => {
    if (!formData.unit_id) return;

    setData(prev => ({
      ...prev,
      standards: []
    }));

    setFormData(prev => ({
      ...prev,
      standard_id: []
    }));

    api.get(`api/teach/${Number(formData.unit_id)}/standards/`)
      .then(response => setData(prev => ({
        ...prev,
        standards: response.data,
      })))
      .catch((error) => console.error("Error Unuts:", error));
  }, [formData.unit_id]);


  return (
    <div className={styles.container}>
      <Border style='Teach_create' bgColor="white" >
      <LoadingOverlay loading={loading}/>
        <div className={styles.content_container}>
          <h3>교수안 생성</h3>
          <SelectContainer data={data} onChange={handleSelectChange} />
          <ChekContainer title="단원"
            optionsList={data.units}
            allowDuplicates={false}
            onChange={(value) => handleSelectChange("unit_id", value)}
            selectedIds={formData.units_id} />
          <ChekContainer style="checkbox_large"
            title="성취기준"
            optionsList={data.standards}
            allowDuplicates={true}
            onChange={(value) => handleSelectChange("standard_id", value)}
            selectedIds={formData.standard_id}
          />
          <ButtonContainer formData={formData} setLoading={setLoading}/>
        </div>
      </Border>
    </div>
  )
}

export default TeachCreate