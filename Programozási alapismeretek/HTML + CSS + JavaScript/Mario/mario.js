let mario = document.getElementById("mario")
let marioX = 0
let marioY = 0

function horizontal(x){
    if (marioY + x < 600 && marioY + x >= 0){
        marioY += x
        mario.style.top = marioY + "px"
    }
}

function vertical(x){
    if (marioX + x < 800 && marioX + x >= 0){
        marioX += x
        mario.style.left = marioX + "px"
    }
    if (x<0)
    mario.innerHTML += "<style>#mario{transform:scaleX(-1);}</style>"
    else
    mario.innerHTML += "<style>#mario{transform:scaleX(1);}</style>"
}