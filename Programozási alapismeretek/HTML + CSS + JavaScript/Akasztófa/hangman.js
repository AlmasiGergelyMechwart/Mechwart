let buttonHolder = document.getElementById("right-wrapper")
let statusHolder = document.getElementById("status")

let letters = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ"

let word = "ALMALÉ"

//let words[] = {"asd", "asddki"}

let mistake = 0;

for(let i=0; i<letters.length; i++){
    buttonHolder.innerHTML += '<button onclick="letterButtonClicked(this)">'+letters[i]+'</button>'
}

for(let i=0; i<word.length; i++){
    if(!letters.includes(word[i]))
    statusHolder.innerText += word[i]
    else
    statusHolder.innerText += "_";
}

function letterButtonClicked(button){
    button.disabled = true;

    let letter = button.innerText;

    if(word.includes(letter)){
        let actual = document.getElementById("status").innerText
        let newStatus = ""
        let blank = 0;

        for(let i=0; i<word.length; i++){
            if(word[i] == letter){
                newStatus += letter
            }else{
                if (actual[i]=="_")
                blank++

                newStatus += actual[i]
            }
        }

        document.getElementById("status").innerText = newStatus

        if (blank == 0){
            document.getElementById("body").innerHTML = `<div><h1>Győztél!</h1><h1>A szó "<span id="word"></span>" volt</h1></div><style>div{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:100%;}h1{font-size:100px;text-align:center;margin:auto;}</style>`
            document.getElementById("word").innerText = word
        }
    }
    else{
        mistake++;
        document.getElementById("left-wrapper").innerHTML = `<img src="stages/${mistake}.png">`
        if(mistake>=10){
            document.getElementById("body").innerHTML = `<div><img src="stages/10.png"><h1>Vesztettél!</h1></div><style>div{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);}img{display:block;margin:auto;}h1{font-size:100px;text-align:center;margin:auto;}</style>`
        }
    }
}