// view more content in section
const moreBtn = document.querySelectorAll("#view-more");
const infoDiv = document.getElementById("more-content");
const selectBtn = document.querySelectorAll("#select-section-btn");
// for navigation
const divBtnSelection = document.getElementById("btn-selection-div");
const salesSection = document.getElementById("sales-section");
const farmSection = document.getElementById("farmer-section");
//for more sales
const moreSales= document.querySelectorAll("#dropdown-btn-best-sellers");
//check existence of report
const loadedDocsCheck = document.getElementById("list-detail");
const loaderBackend = document.getElementById("when-loading");
// add events
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
selectBtn.forEach(
    (elem) => {
        elem.addEventListener("click", (e) =>{
            e.preventDefault();
            if (e.target.innerHTML === "sales") {
                salesSection.style.display = "grid";
                farmSection.style.display = "none";
            } else {
                salesSection.style.display = "none";
                farmSection.style.display = "flex";
            }
        });
    }
);

moreSales.forEach((elem) => {
    elem.addEventListener("click", (e) => {
        e.preventDefault();
        if (e.target === e.target.parentNode.childNodes[5]) {
            e.target.parentNode.childNodes[7].classList.add("active-dropdown");
            e.target.parentNode.childNodes[3].style.display = "inline";
        } else {
            e.target.parentNode.childNodes[5].classList.add("active-dropdown");
            e.target.parentNode.childNodes[3].style.display = "none";
        }
        
        if (e.target.classList[1] !== "active-dropdown") {
            e.target.classList.add("active-dropdown");
        } else {
            e.target.classList.remove("active-dropdown");
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