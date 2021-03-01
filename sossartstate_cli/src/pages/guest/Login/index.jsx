import React, { useState } from 'react'
import { useHistory } from 'react-router-dom'
import { Input, Tooltip, Button, Row, Col } from 'antd'
import {
  InfoCircleOutlined,
  UserOutlined,
  EyeTwoTone,
  EyeInvisibleOutlined,
  KeyOutlined,
  PoweroffOutlined,
} from '@ant-design/icons'
import { useForm, Controller } from 'react-hook-form'
import './index.css'
import { Content, Container } from './style.js'
import banner from 'assests/images/authentication.jpg'
import { login } from '_api/login.api'

const Login = () => {
  const history = useHistory()
  const { control, handleSubmit } = useForm()
  const [loading, setLoading] = useState(false)
  const onSubmit = async ({ email, password }) => {
    try {
      const logedInfo = await login(email, password)
      setLoading(false)
      history.push('/dashboard')
    } catch (error) {}
  }
  return (
    <Container>
      <Row style={{ height: '100%' }}>
        <Col span={16}>
          <div className="crop-image">
            <img src={banner} alt="login banner" />
          </div>
        </Col>
        <Col span={8}>
          <Content>
            <form
              onSubmit={handleSubmit(onSubmit)}
              style={{ textAlign: 'center' }}
            >
              <Controller
                name="email"
                control={control}
                defaultValue=""
                render={({ onChange, value }) => (
                  <Input
                    style={{ marginBottom: '10px' }}
                    onChange={onChange}
                    value={value}
                    placeholder="Correo"
                    prefix={<UserOutlined className="site-form-item-icon" />}
                    suffix={
                      <Tooltip title="Ingresa tu correo">
                        <InfoCircleOutlined
                          style={{ color: 'rgba(0,0,0,.45)' }}
                        />
                      </Tooltip>
                    }
                  />
                )}
              />
              <Controller
                name="password"
                control={control}
                defaultValue=""
                render={({ onChange, value }) => (
                  <Input.Password
                    onChange={onChange}
                    value={value}
                    prefix={<KeyOutlined className="site-form-item-icon" />}
                    placeholder="Ingresa tu contraseña"
                    iconRender={(visible) =>
                      visible ? <EyeTwoTone /> : <EyeInvisibleOutlined />
                    }
                  />
                )}
              />
              <Button
                type="primary"
                htmlType="submit"
                icon={<PoweroffOutlined />}
                loading={loading}
                onClick={() => setLoading(true)}
                style={{ marginTop: '20px' }}
              >
                Entrar
              </Button>
            </form>
          </Content>
        </Col>
      </Row>
    </Container>
  )
}

export default Login
