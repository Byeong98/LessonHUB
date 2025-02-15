import React from 'react'
import { useParams } from 'react-router-dom';
import styles from './TeachDetail.module.css'

import Border from '../Border/Border'

const TeachDetail = () => {
  const { id } = useParams(); // id값 가져오기


  return (
    <div className={styles.container}>
      <Border style='Teach_create' bgColor="white" >
        <div className={styles.content_container}>
          <h3>교수안</h3>
          <div>
            내용
          </div>
        </div>
      </Border>
    </div>
  )
}

export default TeachDetail