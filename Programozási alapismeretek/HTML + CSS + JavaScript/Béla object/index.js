let bela = {
    vnev: "Szabó",
    knev: "Béla",
    kor: 29,
    teljesNev: function() {
        return this.vnev + " " + this.knev;
    },
    kocsi: {
        szin: "kék",
        marka: "Ford",
    },
}

let text = document.getElementById("text")

text.innerText
    += bela.teljesNev() + `\n`
    + bela.kocsi.szin