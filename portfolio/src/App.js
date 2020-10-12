import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
// TODO:
// create headbar that moves
// create different boxes for headbar nav
// start thinking of what to put
// 
// 
// 
// 
// 
// 
// 

function App() {
  return (
    <div className="App">
      <div class="topnav">
        <a class="active" href="#home">Home</a>
        <a href="#news">News</a>
        <a href="#contact">Contact</a>
        <a href="#about">About</a>
      </div>
    </div>
  );
}

export default App;
