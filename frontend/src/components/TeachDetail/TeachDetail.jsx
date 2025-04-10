import React, { useContext, useState, useEffect } from 'react'
import { useParams } from 'react-router-dom';
import styles from './TeachDetail.module.css';
import { useNavigate } from 'react-router-dom';


import Border from '../Border/Border'
import ApiClient from '../../ApiClient';
import { AuthContext } from '../../AuthProvider';
import Button from '../Button/Button';


const DataContent = ({ title, data }) => {
  return (
    <div className={styles.content}>
      <h4>{title}</h4>
      <Border sty="teach_detail" bgColor="rgba(245,245,245,1)">
        {data &&
          data.split(".").map((item, index) => (
            item && item
              .replace(/^,/, "") // 앞에 있는 쉼표 제거
              .replace(/^\d+\s*/, "") // 숫자만 있는 경우 제거
              .trim() // 남아있는 공백 제거
            !== "" && ( // 빈 항목을 필터링
              <p key={index}>
                - {item.replace(/^,/, "")}.
              </p>
            )
          ))}
      </Border>
    </div>
  );
};
const DataUrl = ({ title, data }) => {

  return (
    <div className={styles.content}>
      <h4>{title}</h4>
      <Border sty="teach_detail" bgColor="rgba(245,245,245,1)">
        {data && data.map((item, index) => (
          <p key={index}>
            <a href={item.url}>{item.name}</a>
          </p>
        ))}

      </Border>
    </div>
  );
};

const ButtonContainer = ({ id, data }) => {
  const navigate = useNavigate();
  // const { accessToken } = useContext(AuthContext);
  return (
    <div className={styles.button_container}>
      <Button
        width="40%"
        color='black'
        onClick={() => navigate(`/teach/update/${id}/`, { state: { data } })}
      >
        수정
      </Button>
      <Button
        width="40%"
        onClick={() => navigate("/")}
      >
        나가기
      </Button>
    </div>
  )
}


const TeachDetail = () => {
  const { id } = useParams(); // id값 가져오기
  const { accessToken } = useContext(AuthContext);
  const [data, setData] = useState([]);

  useEffect(() => {
    if (!id) return;
    if (!accessToken) return;

    ApiClient.get(`api/teach/get/${id}/`,
      {
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${accessToken}`,
        }
      }
    )
      .then(response => setData(response.data))
      .catch((error) => console.error("Error fetching data:", error));
  }, [id, accessToken]);

  return (
    <div className={styles.container}>
      <Border sty='teach_detail_form' bgColor="white" >
        <div className={styles.content_container}>
          <h3>{data.title}</h3>
          <div className={styles.top_container}>
            <div>
              <p>
                <span>학년 : </span>
                {data.grade}
              </p>
              <p>
                <span>과목 : </span>
                {data.subject} / {data.section}
              </p>
            </div>
            <div>
              <p>
                <span>단원 : </span>
                {data.unit}
              </p>
              <p>
                <span>작성일 : </span>
                {data.date}
              </p>
            </div>
          </div>
          <DataContent title="학습목표" data={data.objective} />
          <DataContent title="도입" data={data.intro} />
          <DataContent title="전개" data={data.deployment} />
          <DataContent title="정리" data={data.finish} />
          <DataUrl title="참고자료" data={data.url} />
        </div>
        <ButtonContainer id={id} data={data} />
      </Border>
    </div>
  )
}

export default TeachDetail