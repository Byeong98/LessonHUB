import React from 'react'
import { useParams } from 'react-router-dom';
import styles from './TeachDetail.module.css'

const TeachDetail = () => {
  const { id } = useParams(); // id값 가져오기

  return (
    <div>id : {id}</div>
  )
}

export default TeachDetail