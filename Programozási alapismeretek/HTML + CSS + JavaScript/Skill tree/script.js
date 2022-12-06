function randomStats(){
    setStrength(Math.floor(Math.random() * 5) + 1)  //1 - 5
    setEndurance(Math.floor(Math.random() * 5) + 1) //1 - 5
    setAgility(Math.floor(Math.random() * 5) + 1)   //1 - 5
    setSpeed(Math.floor(Math.random() * 5) + 1)     //1 - 5
    setXp(Math.floor(Math.random() * 10) + 6)       //5 - 15
}

let xpP = document.getElementById("xpP")

function setStrength(number){
    let strength = document.getElementById("strength")

    if(number == null){
        if(strength.innerText*1 <= 9 && xpP.innerText*1 >= 1){
            strength.innerText = strength.innerText * 1 + 1
            xpP.innerText = xpP.innerText * 1 - 1
        }
    }else{
        strength.innerText = number * 1
    }

    let dmg = document.getElementById("damage")

    dmg.innerText = strength.innerText*1 * 10
}

function setEndurance(number){
    let endurance = document.getElementById("endurance")

    if(number == null){
        if(endurance.innerText*1 <= 9 && xpP.innerText*1 >= 1){
            endurance.innerText = endurance.innerText * 1 + 1
            xpP.innerText = xpP.innerText * 1 - 1
        }
    }else{
        endurance.innerText = number * 1
    }

    let hp = document.getElementById("hp")

    hp.innerText = endurance.innerText*1 * 10
}

function setAgility(number){
    let agility = document.getElementById("agility")

    if(number == null){
        if(agility.innerText*1 <= 9 && xpP.innerText*1 >= 1){
        agility.innerText = agility.innerText * 1 + 1
        xpP.innerText = xpP.innerText * 1 - 1
    }
    }else{
        agility.innerText = number * 1
    }

    let dodge = document.getElementById("dodge")

    dodge.innerText = agility.innerText*1 * 5
}

function setSpeed(number){
    let speed = document.getElementById("speed")

    if(number == null){
        if(speed.innerText*1 <= 9 && xpP.innerText*1 >= 1){
        speed.innerText = speed.innerText * 1 + 1
        xpP.innerText = xpP.innerText * 1 - 1
    }
    }else{
        speed.innerText = number * 1
    }

    let mspeed = document.getElementById("mspeed")

    mspeed.innerText = speed.innerText*1 * 10
}

function setXp(number){
    if(number == null){
        if(xpP.innerText*1 >= 1){
        xpP.innerText = xpP.innerText * 1 - 1
    }
    }else{
        xpP.innerText = number * 1
    }
}

randomStats();