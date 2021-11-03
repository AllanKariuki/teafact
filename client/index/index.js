//svg animation
const svgText = document.getElementById("svg-text");
//dropdown
const dropDoc = document.getElementById("dropdown-farmer");
const farmerDropHover = document.getElementById("hide-div");
//navigation
const navHider = document.getElementById("nav-btn-hider");
const cross = document.getElementById("cross");
const mainNav = document.querySelector(".main-nav");
const mainBody = document.querySelector(".main-body");
const menu = document.getElementById("menu");
//image scrolling
const radios = document.querySelectorAll("#radio-btn");
/* const reviews = document.querySelectorAll(".div-image");
const search = document.getElementById("searchBtn");
const navBtn = document.getElementById("#nav-btn");
const navBody = document.querySelectorAll(".nav-body"); */
//event listeners
//animate svg


document.addEventListener("scroll", () => {
animate();
    // fetch('http://localhost:5000/all')
    // .then(response=>response.json())
    // .then(data=> loadHTMLTable(data['data']));
});
function animate() {
    var text = "12526";
    function print(str) {
        var i = 0;
        (function main() {
            var char = str[i++];
            svgText.innerHTML += char;
            if(i<str.length)
            setTimeout(main, 600);
        })();
    }
    print(text);
}
//dropdown
farmerDropHover.addEventListener("mouseover", (e) => {
    e.preventDefault();
    dropDoc.classList.add("dropdown-farmer-active");
});
farmerDropHover.addEventListener("mouseout", (e) => {
    e.preventDefault();
    dropDoc.classList.remove("dropdown-farmer-active");
});
//main-nav-active
menu.addEventListener("click", (e) => {
    e.preventDefault();
    mainNav.classList.add("main-nav-active");
    mainBody.classList.add("main-body-with-nav");
});
cross.addEventListener("click", (e) => {
    e.preventDefault();
    mainNav.classList.remove("main-nav-active");
    mainBody.classList.remove("main-body-with-nav");
});
function waitLoader() {
    radios.forEach((elem) => {
        elem.checked = false;
    });
    var i = Math.floor(Math.random() * 4);
    radios[i].checked = true;
}//hover menu
menu.addEventListener("mouseenter", (e) => {
    e.preventDefault();
    mainNav.classList.add("main-nav-active-hover");
    mainBody.classList.add("main-body-nav-normal-display");
});
navHider.addEventListener("click",(e)=> {
    e.preventDefault();
    mainNav.classList.remove("main-nav-active-hover");
    mainBody.classList.remove("main-body-nav-normal-display");
});
// menu.addEventListener("mouseout", (e) => {
//     e.preventDefault();
//     mainNav.classList.remove("main-nav-active-hover");
//     mainBody.classList.remove("main-body-nav-normal-display");
// });
// if (window.screen.width <= 800) {
//     menu.removeEventListener("mouseout");
//         menu.removeEventListener("mouseover");
// }
//to open when ready
/* window.addEventListener("load", (e) => {
    setInterval(waitLoader, 5000);
}); */


//other events
/* navBtn.addEventListener("click", (e) => {
    e.target.preventDefault();
        navBody.forEach((elem) => {
            elem.classList.add("hidden");
        });
    console.log("clicked");
}); */

//xhr calls
/* search.addEventListener("input", (e) => {
    var str = e.value;
    if (str.length == 0) {
        document.getElementById("txtHint").innerHTML = "";
        return;
      } else {
        const xmlhttp = new XMLHttpRequest();
        xmlhttp.onload = function() {
          document.getElementById("txtHint").innerHTML = this.responseText;
        }
      xmlhttp.open("GET", "index.php?q=" + str);
      xmlhttp.send();
      }
}); */

//search
/* const searchBtn = document.querySelector('#submit-farmer');

searchBtn.addEventListener("click", (e)=>{
    e.preventDefault();
    const searchValue =  document.querySelector("#search-farmer").value;
     fetch('http://localhost:5000/search/'+ searchValue.trim())
    .then(response => response.json())
    .then(data=>loadHTMLTable(data['data']));

})
    
//load all data
function loadHTMLTable(data){
    const table = document.querySelector(".results-article table tbody");
    if(data.length === 0){
       table.innerHTML = "<tr><td class='no-data' colspan = '5'>No Data</td></tr>"
       return;
    }
    let tableHtml ="";
    data.forEach(function({first_name, second_name, farm, location, Time}){
        tableHtml+= "<tr>";
        tableHtml+= `<td> ${first_name} ${second_name} </td>`;
        tableHtml+= `<td> ${location}</td>`;
        tableHtml+= `<td> ${farm}</td>`;
        tableHtml+= `<td> ${Time} </td>`;
        tableHtml+= "</tr>";
    });
    table.innerHTML = tableHtml;
}


 */