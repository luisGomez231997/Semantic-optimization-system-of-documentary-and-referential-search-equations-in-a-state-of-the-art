import "../assests/css/App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Dashboard from "../pages/dashboard/dashboard";
import Session from "../pages/session/session";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path="/">
            <Dashboard />
          </Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
