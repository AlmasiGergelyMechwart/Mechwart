let rock = {
    name: 'Rock',
    emoji: '&#9994'
};
let paper = {
    name: 'Paper',
    emoji: '&#9995'
};
let scissors = {
    name: 'Scissors',
    emoji: '&#9996'
};

let choiceButtons = document.getElementsByClassName('choice-button');
choiceButtons[0].innerHTML = rock.emoji;
choiceButtons[1].innerHTML = paper.emoji;
choiceButtons[2].innerHTML = scissors.emoji;

let player = document.getElementById('player-choice').firstChild;
let enemy = document.getElementById('enemy-choice').firstChild;

let playerChoice;
let enemyChoice;

function choiceButtonClicked(emoji) {
    shake();
    player.addEventListener("animationend", function() {
        player.innerHTML = emoji.innerHTML
        if (emoji.innerHTML == rock.emoji)
            playerChoice = 1
        else if (emoji.innerHTML == paper.emoji)
            playerChoice = 2;
        else if (emoji.innerHTML == scissors.emoji)
            playerChoice = 3;
        enemyChoose();
        result();
    })
}

function enemyChoose() {
    let random = Math.floor(Math.random()*3)
    if (random == 0){
        enemy.innerHTML = rock.emoji
    } else if (random == 1){
        enemy.innerHTML = paper.emoji
    } else{
        enemy.innerHTML = scissors.emoji
    }
}

function shake() {
    player.innerHTML = rock.emoji;
    enemy.innerHTML = rock.emoji;

    player.style.animation = "none"
    enemy.style.animation = "none"
    setTimeout(() => {
        player.style.animation = "shake .6s 4"
        enemy.style.animation = "shake .6s 4"
    }, 1);
}

function result() {

}