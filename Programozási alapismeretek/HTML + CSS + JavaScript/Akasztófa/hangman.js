let buttonHolder = document.getElementById("right-wrapper")
let status = document.getElementById("status")

let letters = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"

let word = "ALMALÉ"

for(let i=0; i<letters.length; i++){
    buttonHolder.innerHTML += '<button onclick="letterButtonClicked(this)">'+letters[i]+'</button>'
}

for(let i=0; i<word.length; i++){
    status.innerText += "_";
}

function letterButtonClicked(button){
    button.disabled = true;

    let letter = button.innerText;

    if(word.includes(letter))
        alert("Benne van!")
    else
        alert("Nincs benne!")
}