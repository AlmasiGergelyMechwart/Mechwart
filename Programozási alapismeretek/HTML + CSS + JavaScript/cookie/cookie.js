let points = document.getElementById("points");
let point = 1;
let grandmaPrice = 100;

function cookieClicked() {
    points.innerText = points.innerText * 1 + point;
}

function buyGrandma() {
    if (points.innerText * 1 >= grandmaPrice) {
        points.innerText = points.innerText * 1 - grandmaPrice;
        grandmaPrice = Math.floor(grandmaPrice * 1.5);
        document.getElementById("grandmaPrice").innerText = grandmaPrice
        point++;
    } else {
        alert("Nincs elég pontod a nagyira!");
    }
}

function buyCookie() {
    if (points.innerText * 1 >= 2) {
        points.innerText = points.innerText * 1 - 2;
        points.innerText = points.innerText * 1 + 1;
    } else {
        alert("Nincs elég pontod a sütire!");
    }
}