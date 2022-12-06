let foszam = document.getElementById("foszam")
let tej = document.getElementById("tej")
let tojas = document.getElementById("tojas")
let cukor = document.getElementById("cukor")

function frissit(){
    tej.innerText = foszam.value * 0.2
    tojas.innerText = foszam.value * 2
    cukor.innerText = foszam.value * 1
}

frissit()