import "../assests/css/App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Dashboard from "../pages/dashboard/dashboard.jsx";
import Session from "../pages/session/session";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/">
          <Dashboard />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
