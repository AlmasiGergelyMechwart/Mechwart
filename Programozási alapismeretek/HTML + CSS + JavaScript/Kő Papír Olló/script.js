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
    document.getElementById("endText").innerText = "";
    shake();
    player.addEventListener("animationend", function() {
        player.style.animation = "none"
        enemy.style.animation = "none"
        player.innerHTML = emoji.innerHTML
        playerChoice = emoji.classList.item(1)
        enemyChoose();
        result();
    }, {once : true})
}

function enemyChoose() {
    switch (Math.floor(Math.random()*3)) {
        case 0:
            enemy.innerHTML = rock.emoji
            enemyChoice = 1
            break;
        case 1:
            enemy.innerHTML = paper.emoji
            enemyChoice = 2
            break;
        case 2:
            enemy.innerHTML = scissors.emoji
            enemyChoice = 3
            break;
    }
}

function shake() {
    player.innerHTML = rock.emoji;
    enemy.innerHTML = rock.emoji;

    player.style.animation = "shake .6s 4"
    enemy.style.animation = "shake .6s 4"
}

function result() {
    if (playerChoice == enemyChoice) {
        document.getElementById("endText").innerText = "Döntetlen";
    } else if (playerChoice == enemyChoice+1 || playerChoice == enemyChoice-2) {
        document.getElementById("endText").innerText = "Győztél";
    } else if (playerChoice == enemyChoice-1 || playerChoice == enemyChoice+2) {
        document.getElementById("endText").innerText = "Vesztettél";
    }
}