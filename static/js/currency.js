$(document).ready(function() {
    let x = document.querySelectorAll(".currency");
    console.log(x)
    
    for (let i = 0, len = x.length; i < len; i++) {
        let num = Number(x[i].innerHTML)
                .toLocaleString('en');
                console.log(num)
                
        x[i].innerHTML = num;

        x[i].classList.add("poundSign");
    }

});
