function saySg(){
    console.log("Something")
}

function greetSb(name){
    console.log(`Hello ${name}!`)
}

function canDrink(age){
    /*if (age >= 18){
        return true
    }
    else{
        return false
    }*/

    return age >= 18
}

function calculateAge(yearOfBirth){
    return 2023 - yearOfBirth
}

let belaCanDrink = canDrink(calculateAge(2004))
console.log(belaCanDrink)

let ageSlider = document.getElementById("ageSlider")

function sliderMove(slider){
    document.getElementById("sliderValue").innerText = slider.value
    
    if (canDrink(slider.value))
    document.body.style.backgroundColor = "green"
    else
    document.body.style.backgroundColor = "red"
}

setInterval(() => {
    ageSlider.value = ageSlider.value*1 + 1
    sliderMove(ageSlider)
}, 500);

sliderMove(ageSlider)