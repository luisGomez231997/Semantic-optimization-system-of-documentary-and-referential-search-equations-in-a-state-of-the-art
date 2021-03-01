import { config } from '_config'

export const login = (email, password) => {
  console.log(email, password)
  return fetch(`${config.apiUrl}/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      email,
      password,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error('Login fallido')
      }
      return response
    })
    .then((response) => response.json())
    .then((data) => data.data)
}
