import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Dashboard from './pages/dashboard/dashboard.jsx'
//import Session from './pages/session/session.jsx'
import Login from './pages/guest/Login'

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/dashboard/">
          <Dashboard />
        </Route>
        {/* <Route exact path="/">
          <Session />
        </Route> */}
        <Route exact path="/login">
          <Login />
        </Route>
      </Switch>
    </Router>
  )
}

export default App
