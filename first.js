let logo = document.querySelector("#icon");
let close1 = document.querySelector("#close");
let dialog  = "closed";
console.log("helol");
function open(){
   document.querySelector("#dialogindex").style.display = "flex"
};
function close(){
   document.querySelector("#dialogindex").style.display = "none"
};

logo.addEventListener("click",open);
close1.addEventListener("click",close);