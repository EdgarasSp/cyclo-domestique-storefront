$(document).ready(function() {
    let x = document.querySelectorAll(".currency");
    
    for (let i = 0, len = x.length; i < len; i++) {
        let num = Number(x[i].innerHTML)
                .toLocaleString('en');
                
        x[i].innerHTML = numto.Fixed(2);
        x[i].classList.add("poundSign");
    }

});
