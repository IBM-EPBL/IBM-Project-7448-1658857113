// document.addEventListener("load", function() {
//     const wrapper = document.querySelector(".loader-wrapper");
//     wrapper.fadeOut("slow");
// })

const fileName = localStorage.getItem("fileName");
// alert(fileName);
const fName = document.querySelector(".pred");
fName.innerHTML = "PREDICTION: " +fileName;

setTimeout(function(){
    const loader = document.querySelector(".loader");
    loader.classList.add("hide-loader");
}, 2000);

setTimeout(function(){
    const pred = document.querySelector(".pred");
    pred.classList.remove("pred-remove");
}, 2000);

// const pred = document.querySelector(".pred");

// setTimeout(function(){
//     pred.classList.add(".pred-remove");
// }, 2);