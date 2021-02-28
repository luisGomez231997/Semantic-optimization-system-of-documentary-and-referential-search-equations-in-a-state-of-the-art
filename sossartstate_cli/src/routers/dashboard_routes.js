import "../assests/css/App.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function DashboardRouter() {
  return (
    <Router>
      <Switch>
        <Route exact path="profile" />
        <Route exact path="log-out" />
        <Route exact path="H-graph" />
        <Route exact path="kw-graph" />
        <Route exact path="w-graph" />
        <Route exact path="write-eq" />
        <Route exact path="assemble-eq" />
        <Route exact path="data-store" />
      </Switch>
    </Router>
  );
}

export default DashboardRouter;
