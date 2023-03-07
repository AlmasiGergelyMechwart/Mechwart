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

function choiceButtonClicked(emoji) {
    document.getElementById('player-choice').innerHTML = emoji.innerHTML
    enemyChoice();
}

function enemyChoice() {
    let random = Math.floor(Math.random()*3)
    if (random == 0){
        document.getElementById('enemy-choice').innerHTML = rock.emoji
    } else if (random == 1){
        document.getElementById('enemy-choice').innerHTML = paper.emoji
    } else{
        document.getElementById('enemy-choice').innerHTML = scissors.emoji
    }
}