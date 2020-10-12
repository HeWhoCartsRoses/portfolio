import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
// TODO:
// bare bones idea of what to make
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
        <a class="active" href="#top">Top</a>
        <a href="#about">About Me</a>
        <a href="#news">Portfolio</a>
        <a href="#contact">Contact</a>
      </div>
      <div class="about">
        <p class="head">about me!</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Turpis egestas integer eget aliquet nibh praesent. Tortor posuere ac ut consequat semper viverra. Turpis egestas integer eget aliquet nibh praesent tristique magna sit. Euismod quis viverra nibh cras pulvinar. Ipsum suspendisse ultrices gravida dictum fusce ut placerat orci. Aliquam sem et tortor consequat id porta. Ultricies integer quis auctor elit. Parturient montes nascetur ridiculus mus. Senectus et netus et malesuada. Penatibus et magnis dis parturient montes nascetur. Eros in cursus turpis massa tincidunt dui ut ornare. Diam in arcu cursus euismod quis viverra nibh cras pulvinar. Porttitor eget dolor morbi non arcu risus quis varius.</p>
      </div>
      <div class="portfolio">
        <p class="head">stuff ive worked on!</p>
        <p>Feugiat in fermentum posuere urna nec tincidunt praesent semper feugiat. Dui id ornare arcu odio ut sem nulla pharetra. Ultricies integer quis auctor elit. Venenatis urna cursus eget nunc scelerisque viverra. A iaculis at erat pellentesque adipiscing commodo elit at imperdiet. Congue quisque egestas diam in arcu cursus. Sapien eget mi proin sed libero. Ultricies leo integer malesuada nunc vel risus commodo viverra. Mi ipsum faucibus vitae aliquet. Amet consectetur adipiscing elit duis tristique sollicitudin nibh sit. Sapien pellentesque habitant morbi tristique senectus et netus. Iaculis urna id volutpat lacus laoreet non. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Cursus vitae congue mauris rhoncus aenean vel elit scelerisque. Feugiat nibh sed pulvinar proin gravida hendrerit lectus. Urna porttitor rhoncus dolor purus. Tortor at risus viverra adipiscing at in. Amet justo donec enim diam vulputate ut pharetra sit.</p>
      </div>
      <div class="contact">

        <p class="head">how to reach me!</p>
        <p>In nulla posuere sollicitudin aliquam ultrices sagittis orci. Sollicitudin tempor id eu nisl nunc mi ipsum faucibus vitae. Vestibulum lorem sed risus ultricies tristique nulla aliquet enim tortor. Mi proin sed libero enim. Enim sit amet venenatis urna cursus eget nunc scelerisque. Cras adipiscing enim eu turpis egestas pretium aenean. Imperdiet sed euismod nisi porta lorem mollis aliquam ut porttitor. Vestibulum lorem sed risus ultricies tristique. Enim ut sem viverra aliquet eget sit amet tellus cras. Cursus mattis molestie a iaculis at erat pellentesque. Quisque id diam vel quam.</p>
      </div>
    </div>
  );
}

export default App;
