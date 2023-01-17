let buttonHolder = document.getElementById("right-wrapper")
let status = document.getElementById("status")

let letters = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"

let word = "ALMALÉ"

let mistake = 0;

for(let i=0; i<letters.length; i++){
    buttonHolder.innerHTML += '<button onclick="letterButtonClicked(this)">'+letters[i]+'</button>'
}

for(let i=0; i<word.length; i++){
    status.innerText += "_";
}

function letterButtonClicked(button){
    button.disabled = true;

    let letter = button.innerText;

    if(word.includes(letter)){
        let actual = document.getElementById("status").innerText
        let newStatus = ""

        for(let i=0; i<word.length; i++){
            if(word[i] == letter){
                newStatus += letter
            }else{
                newStatus += actual[i]
            }
        }

        document.getElementById("status").innerText = newStatus
    }
    else{
        mistake++;
        document.getElementById("left-wrapper").innerHTML = `<img src="stages/${mistake}.png">`
        if(mistake>=10){
            document.getElementById("body").innerHTML = `<div><img src="stages/10.png"><h1>Vesztettél</h1></div><style>div{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);}h1{font-size:100px;text-align:center;}</style>`
        }
    }
}