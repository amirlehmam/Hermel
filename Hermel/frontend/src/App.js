import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import EmailInterface from './components/EmailInterface';  // Assurez-vous que le chemin est correct
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <Switch>
            <Route path="/email-interface" component={EmailInterface} />
            <Route path="/">
              <p>
                Edit <code>src/App.js</code> and save to reload.
              </p>
              <a
                className="App-link"
                href="https://reactjs.org"
                target="_blank"
                rel="noopener noreferrer"
              >
                Learn React
              </a>
            </Route>
          </Switch>
        </header>
      </div>
    </Router>
  );
}

export default App;
