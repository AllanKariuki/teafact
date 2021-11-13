const moreBtn = document.querySelectorAll("#view-more");
const infoDiv = document.getElementById("more-content");
//check existence of report
const loadedDocsCheck = document.getElementById("list-detail");
const loaderBackend = document.getElementById("when-loading");
//events
moreBtn.forEach((elem) => {
    elem.addEventListener("click", (e) => {
        e.preventDefault();
        if (e.target.innerHTML === "view" ) {
            e.target.innerHTML = "less";
            e.target.classList.add("active-btn");
            e.target.parentNode.childNodes[9].classList.add("active");
        } else {
            e.target.innerHTML = "view";
            e.target.classList.remove("active-btn");
            e.target.parentNode.childNodes[9].classList.remove("active");
        }
        
    });
});

document.addEventListener("DOMContentLoaded", () => {
    if (loadedDocsCheck.childElementCount <=  2)
    {
        loaderBackend.classList.add("activeLoader");
    } else {
        loaderBackend.classList.remove("activeLoader");
   }
});