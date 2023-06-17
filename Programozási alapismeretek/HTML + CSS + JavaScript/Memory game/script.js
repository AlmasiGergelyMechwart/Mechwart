let playground = document.getElementById("playground")

let iconList = [
    1,1,
    2,2,
    3,3,
    4,4,
    5,5,
    6,6,
    7,7,
    8,8,
]

iconList = iconList.sort(
    function(a,b){
        let rnd = Math.random() - 0.5;
        return rnd;
    }
)

for (let i = 0; i < iconList.length; i++) {
    let flipBox = document.createElement("div")
    flipBox.classList.add("flip-box")
    playground.appendChild(flipBox)
    let flipBoxInner = document.createElement("div") 
    flipBoxInner.classList.add("flip-box-inner")
    flipBox.appendChild(flipBoxInner)
    let flipBoxFront = document.createElement("div") 
    flipBoxFront.classList.add("flip-box-front")
    flipBoxInner.appendChild(flipBoxFront)
    let flipBoxBack = document.createElement("div") 
    flipBoxBack.classList.add("flip-box-back")
    flipBoxInner.appendChild(flipBoxBack)
    let label = document.createElement("span") 
    flipBoxBack.classList.add("label")
    flipBoxBack.appendChild(label)

    flipBox.onclick = () => {
        if (document.getElementsByClassName("selected").length >= 2) return
        if (flipBox.classList.contains("found")) return;

        label.innerHTML=iconList[i];
        flipBox.classList.add("selected")

        let selectedCards = document.getElementsByClassName("selected")
        if (selectedCards.length != 2) return;

        //TEST

        let cards = [selectedCards[0], selectedCards[1]] 

        let card1 = selectedCards[0]
        let card2 = selectedCards[1]
        
        if (card1.innerHTML == card2.innerHTML){
            for (let i=0; i<2; i++) {
                cards[i].classList.remove("selected")
                cards[i].classList.add("found")
            }
        } else {
            flipBox.addEventListener("transitionend", function() {
                // setTimeout(() => {
                    for (let i=0; i<2; i++) {
                        cards[i].classList.remove("selected")
                    }
                // }, 1000);
            }, {once : true})
        }

        let found = document.getElementsByClassName("found")
        if (found.length == iconList.length) {
            setTimeout(() => {
                for (let i=0; i<found.length; i++) {
                    found[i].style.opacity = 0
                }
            }, 3000);
        }
    }
}

function test() {
    
}