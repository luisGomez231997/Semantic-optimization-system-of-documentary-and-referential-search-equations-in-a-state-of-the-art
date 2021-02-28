import "../assests/css/App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Dashboard from "../pages/dashboard/dashboard.js";
import Session from "../pages/session/session";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/dashboard/">
          <Dashboard />
        </Route>
        <Route exact path="/">
          <Session />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
