import React from 'react'
import styles from './TeachList.module.css'
import { Link } from 'react-router-dom'

import Border from '../Border/Border'

const TeachForm = ({id}) => {
  return (
    <Link to={`/teach/detail/${id}`}> 
      <Border style='TeachingForm' bgColor="rgba(245,245,245,1)">
        <div>
          <p>제목</p>
          <p>학년</p>
          <p>과목</p>
          <p>단원</p>
          <p>성취 기준</p>
        </div>
      </Border>
    </Link>
  )
}

const AddTeachForm = () => {
  return (
    <Link to="/teach/create">
      <Border style='TeachingForm' bgColor="rgba(245,245,245,1)">
        <div>
          <p>+</p>
          <p>추가하기</p>
        </div>
      </Border>
    </Link>
  )
}


const TeachList = () => {
  return (
    <div className={styles.container}>
      <div className={styles.content}>
        <h1>교수안</h1>
        <div className={styles.formWrapper}>
          <AddTeachForm />
          <TeachForm id ={1} />
        </div>
      </div>
    </div>
  )
}

export default TeachList

