$(document).ready(function() {
    let x = document.querySelectorAll(".currency");
    
    for (let i = 0, len = x.length; i < len; i++) {
        let num = Number(x[i].innerHTML).toLocaleString('en');
                
        x[i].innerHTML = num;
        x[i].classList.add("poundSign");
    }

});

// parseFloat(num).toFixed(2)  does not work, either comma (without)or decimals (with)//