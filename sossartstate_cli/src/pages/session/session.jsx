import React from 'react'
import { Row, Col, Image } from 'antd'
import Login from '../_components/form-login'
import banner from '../../assests/images/authentication.jpg'

function Session(props) {
  return (
    <Row>
      <Col span={12}>
        <Image
          src={banner}
          style={{
            width: '100%',
            height: '100%',
          }}
        />
      </Col>
      <Col span={12}>
        <Login />
      </Col>
    </Row>
  )
}

export default Session
