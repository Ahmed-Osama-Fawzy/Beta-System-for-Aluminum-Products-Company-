window.onscroll = function (){
    if (window.scrollY  >= 1000 ){
        document.getElementById("ReturnToTop").style.display = "block" 
    }else{
         document.getElementById("ReturnToTop").style.display = "none"; 
    } 
    document.getElementById("ReturnToTop").onclick = ()=>{
        window.scrollTo({
            top: 0 ,
            behavior: "smooth"
        })
    }
}

let buttonList = document.querySelectorAll(".Del");
console.log(buttonList)
buttonList.forEach(function(i){
i.addEventListener("click", function(e){
    alert(e.classlist);
    })
})

