import main from "./component/main.js";

import "regenerator-runtime";
import "./style.css";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

document.addEventListener("DOMContentLoaded", main);
const navbar = document.querySelector('.navbar');

window.addEventListener("scroll",() => {
    const scrollY = window.screenY;
    if (scrollY < 20) {
        navbar.classList.remove('shawdow-sm');
    } else {
        navbar.classList.add('shadow-sm');
    }
});