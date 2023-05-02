function kockadobas(oldal, dobasokSzama) {
    let ossz = 0
    for (let i=0; i<dobasokSzama; i++) {
        ossz += Math.floor(Math.random()*oldal) + 1
    }
    return ossz
}

//Stength
let strengthElement = document.getElementById("strength")
let strength = kockadobas(6, 2)
strengthElement.innerText = strength

//Defense
let defenseElement = document.getElementById("defense")
let defense = Math.round(strength * 1.7 * 100) / 100
defenseElement.innerText = defense

//Constitution
let constitutionElement = document.getElementById("constitution")
let constitution = kockadobas(3, 3)
constitutionElement.innerText = constitution

//Hit points
let hitPointsElement = document.getElementById("hitPoints")
let hitPoints = Math.round(constitution * 2.2 * 100) / 100
hitPointsElement.innerText = hitPoints

//Dexterity
let dexterityElement = document.getElementById("dexterity")
let dexterity = kockadobas(6, 2)
dexterityElement.innerText = dexterity

//Evasion
let evasionElement = document.getElementById("evasion")
let evasion = Math.round(dexterity * 0.8 * 100) / 100
evasionElement.innerText = evasion

//Luck
let luckElement = document.getElementById("luck")
let luck = kockadobas(50, 1)
luckElement.innerText = luck

//Critical hit
let criticalHitElement = document.getElementById("criticalHit")
let criticalHit = Math.round(luck / 5 * 100) / 100
criticalHitElement.innerText = criticalHit + "%"

//Intelligence
let intelligenceElement = document.getElementById("intelligence")
let intelligence = kockadobas(6, 3)
intelligenceElement.innerText = intelligence

//Damage
let damageElement = document.getElementById("damage")
let damage = Math.round(intelligence * 1.5 * 100) / 100
damageElement.innerText = damage

//Armor
let armorElement = document.getElementById("armor")
let armor = kockadobas(100, 1)
armorElement.innerText = armor

//Damage reduction
let damageReductionElement = document.getElementById("damageReduction")
let damageReduction = Math.round(armor / 2 * 100) / 100
damageReductionElement.innerText = damageReduction + "%"