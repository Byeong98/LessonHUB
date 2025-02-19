import React, { useEffect, useRef, useCallback, useState, useContext } from 'react';
import { useParams, useLocation, useNavigate } from 'react-router-dom';
import styles from "./TeachUpdate.module.css";

import Border from '../Border/Border';
import Button from '../Button/Button';
import api from '../../Api';
import LoadingOverlay from '../LoadingOverlay/LoadingOverlay';
import { AuthContext } from '../../AuthProvider';

const TopContainer = ({ data }) => {
  return (
    <div className={styles.top_container}>
      <div>
        <p><span>학년 : </span>{data.grade}</p>
        <p><span>과목 : </span>{data.subject} / {data.section}</p>
      </div>
      <div>
        <p><span>단원 : </span>{data.unit}</p>
        <p><span>작성일 : </span>{data.date}</p>
      </div>
    </div>
  );
};

const DataContent = ({ title, value, onChange }) => {
  const textRef = useRef(null);
  const [inputValue, setInputValue] = useState(value || ""); 

  // 입력된 데이터를 줄 단위로 변환
  const formattedData = value
    ? value
        .split(".")
        .map((item) =>
          item
            .replace(/^,/, "") 
            .replace(/^\d+\s*/, "")
        )
        .filter((item) => item !== "")
        .join("\n")
    : "";

  const rowCount = formattedData ? formattedData.split("\n").length : 1;

  // 높이 자동 조절 함수
  const adjustHeight = useCallback(() => {
    if (textRef.current) {
      textRef.current.style.height = "auto";
      textRef.current.style.height = textRef.current.scrollHeight + "px";
    }
  }, []);

  useEffect(() => {
    adjustHeight();
  }, [formattedData, adjustHeight]);

  const handleChange = (e) => {
    const newValue = e.target.value;
    setInputValue(newValue); 
    onChange(newValue); 
  };
  if (!inputValue) return;
  return (
    <div className={styles.content}>
      <h4>{title}</h4>
      <textarea
        name={title}
        className={styles.textarea}
        rows={rowCount}
        ref={textRef}
        value={formattedData} 
        onChange={handleChange}
      />
    </div>
  );
};

const ButtonContainer = ({ id, data, setLoading }) => {
  const navigate = useNavigate();
  const { accessToken } = useContext(AuthContext);

  const handlTeachCreate = async () => {
    if (!accessToken) return;

    setLoading(true);
    try {
      const response = await api.put(
        `/api/teach/update/${id}/`,
        data,
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
      width="40%"
      color='black'
      onClick={handlTeachCreate}
    >
      수정 하기
    </Button>
    <Button
      width="40%"
      onClick={() => navigate("/")}
    >
      취소 
    </Button>
  </div>
)
}



const TeachUpdate = () => {
  const { id } = useParams(); // id값 가져오기
  const location = useLocation();
  const Data = location.state?.data || {}; // 초기 데이터
  const [loading, setLoading] = useState(false); 

  const [formData, setFormData] = useState({
    teach_id: id,
    objective: Data.objective || "",
    intro: Data.intro || "",
    deployment: Data.deployment || "",
    finish: Data.finish || "",
  });


  const handleChange = (key, value) => {
    setFormData((prev) => ({
      ...prev,
      [key]: value,
    }));
  };

  
  return (
    <div className={styles.container}>
      <LoadingOverlay loading={loading}/>
      <Border sty="teach_detail_form" bgColor="white">
        <div className={styles.content_container}>
          <h3>교수안(수정)</h3>
          <p className={styles.title}
          ><span>제목: </span>{formData.title}</p>
          <TopContainer data={Data} />
          <DataContent title="학습목표" value={formData.objective} onChange={(val) => handleChange("objective", val)} />
          <DataContent title="도입" value={formData.intro} onChange={(val) => handleChange("intro", val)} />
          <DataContent title="전개" value={formData.deployment} onChange={(val) => handleChange("deployment", val)} />
          <DataContent title="정리" value={formData.finish} onChange={(val) => handleChange("finish", val)} />
        </div>
        <ButtonContainer id={id} setLoading={setLoading} data={formData}/>
      </Border>
    </div>
  );
};

export default TeachUpdate;
