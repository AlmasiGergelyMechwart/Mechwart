console.log("Hello JS");

let elso = 10;
const masodik = 5;

elso = 23;

let areYouHungry = true;

let negyedik;

console.log(areYouHungry);

console.log(typeof(areYouHungry));

if(areYouHungry)
console.log("Egyél!");
else
console.log("Ne egyél!");

const kor = document.getElementById("kor");
const body = document.getElementById("body");
const background = document.getElementsByClassName("background");
const text = document.getElementsByClassName("text");

console.log(typeof(kor));

let felkapcsolva = true;

function katt(){
    felkapcsolva = !felkapcsolva;

    if(felkapcsolva){
        for(let i=0;i<background.length;i++)
            background[i].style.backgroundColor = "black";
        for(let i=0;i<text.length;i++)
            text[i].style.color = "black";
        body.style.backgroundColor = "white";
    }
    else{
        for(let i=0;i<background.length;i++)
            background[i].style.backgroundColor = "white";
        for(let i=0;i<text.length;i++)
            text[i].style.color = "white";
        body.style.backgroundColor = "black";
    }
}