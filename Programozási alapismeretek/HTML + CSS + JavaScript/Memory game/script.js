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



    // let card = document.createElement("div")
    // let label = document.createElement("span")
    // card.classList.add("card")
    // label.classList.add("label")
    // playground.appendChild(card)
    // card.appendChild(label)

    flipBox.onclick = () => {
        if (document.getElementsByClassName("selected").length >= 2) return
        if (flipBox.classList.contains("found")) return;

        label.innerHTML=iconList[i];
        flipBox.classList.add("selected")

        if (document.getElementsByClassName("selected").length == 2) test();
    }
}

function test() {
    let selectedCards = document.getElementsByClassName("selected")

    let cards = [selectedCards[0], selectedCards[1]] 

    let card1 = selectedCards[0]
    let card2 = selectedCards[1]
    
    if (card1.innerHTML == card2.innerHTML){
        card1.classList.remove("selected")
        card2.classList.remove("selected")
        card1.classList.add("found")
        card2.classList.add("found")
        for (let i=0; i<2; i++) {
            cards[i].style.backgroundColor = "black";
        }
        // cards.forEach(card => {
        //     card.style.backgroundColor = "black";
        // });
    } else {
        // flipBox.addEventListener("transitionend", function() {
            setTimeout(() => {
                card1.classList.remove("selected")
                card2.classList.remove("selected")
                selectedCards[0].style.backgroundColor = "black";
                selectedCards[1].style.backgroundColor = "black";
            }, 1000);
        // }, {once : true})
    }

    let found = document.getElementsByClassName("found")
    if (found.length == iconList.length) {
        setTimeout(() => {
            found.forEach(card => {
                card.style.opacity = "0%"
            });
        }, 1000);
    }
}