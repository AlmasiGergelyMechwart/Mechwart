let eredmeny = document.getElementById("eredmeny")

function random(num) {
    return Math.floor(Math.random() * num) + 1
}

function gurit() {
    let oldalszam = document.getElementById("oldalak").value
    let dobasokSzama = document.getElementById("dobasok").value

    // eredmeny.innerText = "|"
    // for (let i=0; i<dobasokSzama; i++) {
    //     eredmeny.innerText += random(oldalszam) + "|"
    // }

    let felso = document.getElementById("felso")
    felso.innerHTML = ""
    felso.style.top = "40%"; //- (Math.floor(dobasokSzama/5)+1) + "0%";
    
    if (dobasokSzama<=25) {
        felso.style.gridTemplateColumns = (dobasokSzama<5) ? `repeat(${dobasokSzama}, 1fr)` : `repeat(5, 1fr)` 
        for (let i=0; i<dobasokSzama; i++) {
            let dobas = document.createElement("h3")
            felso.appendChild(dobas)

            dobas.style.margin = "auto"

            dobas.innerText = random(oldalszam)
        }
    } else {
        felso.style.gridTemplateColumns = 1 
        let dobas = document.createElement("h3")
        felso.appendChild(dobas)
        
        let atlag = 0;
        //a dobasok array egy dobasokszama elemű array amiben minden dobás megtalálható
        let dobasok = [];
        //a dobasok2 array egy oldalakszama elemű array ahhol az index az oldalszám-1 és az értéke hogy hányszor dobték azt a számot
        let dobasok2 = [];
        for (let i=0; i<oldalszam; i++) dobasok2[i] = 0;
        for (let i=0; i<dobasokSzama; i++) {
            let szam = random(oldalszam)
            atlag += szam
            dobasok.push(szam)
            dobasok2[szam-1]++
        }
        console.log(dobasok2)
        atlag /= dobasokSzama;
        atlag = Math.floor(atlag*100) / 100
        //erre tuti van jobb megoldás
        
        //módusz (leggyakoribb adat)
        let bool = true;
        let moduszIndex = [];
        let dobasok2M = dobasok2.slice()
        while (bool) {
            moduszIndex.push(dobasok2M.indexOf(Math.max(...dobasok2M))+1)
            dobasok2M[dobasok2M.indexOf(Math.max(...dobasok2M))] = 0

            if (dobasok2[moduszIndex[moduszIndex.length-1]-1] != Math.max(...dobasok2M)) {
                bool = false
            }
        }

        //medián (sorberendezett sorban a középső adat)
        let rendezettSor = dobasok.slice().sort((a, b) => {return a - b})
        console.log(rendezettSor)
        let median
        if (dobasokSzama%2 == 0)
        median = rendezettSor[rendezettSor.length/2]
        else if (rendezettSor[Math.floor(rendezettSor.length/2)] == rendezettSor[Math.ceil(rendezettSor.length/2)])
        median = rendezettSor[Math.floor(rendezettSor.length/2)]
        else
        median = rendezettSor[Math.floor(rendezettSor.length/2)] + ", " + rendezettSor[Math.ceil(rendezettSor.length/2)]
        console.log(median)

        //kiírás
        dobas.style.fontSize = "2rem"
        dobas.innerHTML += "Átlag: " + atlag;
        dobas.innerHTML += "<br>Módusz: ";
        if (moduszIndex.length != 1) {
            for (let i=0; i<moduszIndex.length-1; i++)
            dobas.innerHTML += moduszIndex[i] + ", ";
            dobas.innerHTML += moduszIndex[moduszIndex.length-1];
        } else
        dobas.innerHTML += moduszIndex[0];
        dobas.innerHTML += "<br>Medián: " + median;
    }
}