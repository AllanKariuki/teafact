const moreBtn = document.querySelectorAll("#view-more");
const infoDiv = document.getElementById("more-content");
const checkState = document.querySelectorAll(".payment-status");
const statusBtn = document.querySelectorAll(".status-btn");
//check existence of report
const loadedDocsCheck = document.getElementById("list-detail");
const loaderBackend = document.getElementById("when-loading");
//events
moreBtn.forEach((elem) => {
    elem.addEventListener("click", (e) => {
        e.preventDefault();
        console.log(e.target.parentNode.childNodes);
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
document.addEventListener("DOMContentLoaded", (e) => {
    checkState.forEach(
        (elem) => {
            if (elem.innerHTML === "paid") {
                elem.style.border = "1px solid rgb(123, 255, 105)";
                elem.style.color = "rgb(123, 255, 105)";
            } else if(elem.innerHTML === "pending"){
                elem.style.border = "1px solid rgb(255, 191, 95)";
                elem.style.color = "rgb(255, 191, 95)";
            } else{
                elem.style.border = "1px solid rgb(253, 89, 89)";
                elem.style.color = "rgb(253, 89, 89)";
            }
        }
    );
    
});
document.addEventListener("DOMContentLoaded", () => {
    if (loadedDocsCheck.childElementCount <=  2)
    {
        loaderBackend.classList.add("activeLoader");
    } else {
        loaderBackend.classList.remove("activeLoader");
   }
});
