import React, { useContext, useEffect, useState } from 'react'
import styles from './TeachList.module.css'
import { Link, useNavigate } from 'react-router-dom'

import Border from '../Border/Border'
import api from '../../Api';
import { AuthContext } from '../../AuthProvider';

const TeachForm = ({ item }) => {

  return (
    <Link to={`/teach/detail/${item.id}`}>
      <Border sty='teach_list' bgColor="rgba(245,245,245,1)">
        <div className={styles.teachForm_padding}>
          <div className={styles.teachForm_container}>
            <p>
              <span>학년 : </span>
              {item.grade}
            </p>
            <p>
              <span>과목 : </span>
              {item.subject} / {item.section}
            </p>
            <p>
              <span>단원 : </span>
              {item.unit}
            </p>
            <div className={styles.titleContainer}>
              <span>제목 </span>
              <p className={styles.truncateText}>{item.title}</p>
            </div>
          </div>
          <div className={styles.dateContainer}>
            <p>{item.date}</p>
          </div>
        </div>
      </Border>
    </Link>
  )
}

const AddTeachForm = ({ token }) => {
  const navigate = useNavigate();

  const handleClick = (e) => {

    if (!token) {
      e.preventDefault(); // 기본 링크 이동 방지
      navigate("/login"); // 로그인 페이지로 이동
    }
  };

  return (
    <Link to="/teach/create" onClick={handleClick}>
      <Border sty="teach_list" bgColor="rgba(245,245,245,1)">
        <div className={styles.add_container}>
          <img src="/add.png" alt="lessonhub" className={styles.addbut} />
          <p>추가하기</p>
        </div>
      </Border>
    </Link>
  );
};


const TeachList = () => {
  const [data, setData] = useState([]);
  const { accessToken } = useContext(AuthContext);

  useEffect(() => {
    if (!accessToken) return;

    api.get(`/api/teach/list/`,
      {
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${accessToken}`,
        }
      }
    )
      .then(response => setData(response.data))
      .catch((error) => console.error("Error fetching data:", error));
  }, [accessToken]);

  return (
    <div className={styles.container}>
      <div className={styles.content}>
        <h1>교수안</h1>
        <div className={styles.formWrapper}>
          <AddTeachForm token={accessToken} />
          {data.length !== 0 ? (
            data.map(item => <TeachForm key={item.id} item={item} />)
          ) : (
            <Border sty='teach_list' bgColor="rgba(245,245,245,1)">
              <div className={styles.add_container}>
                <p></p>
                <p>교수안을 추가하세요.</p>
              </div>
            </Border>
          )}
        </div>
      </div>
    </div>
  );
};

export default TeachList

