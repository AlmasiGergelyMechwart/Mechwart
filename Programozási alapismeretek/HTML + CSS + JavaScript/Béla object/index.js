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

console.log(bela.teljesNev())
console.log(bela.kocsi.szin)