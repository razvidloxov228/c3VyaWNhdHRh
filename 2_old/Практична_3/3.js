let abonement = prompt("У вас є абонемент? (true/false): ").toLowerCase() === 'true';
let balance = Number(prompt("Скільки грошей на рахунку?: "));
if (abonement || balance > 100) {
    console.log("Доступ дозволено");
} else {
    console.log("Доступ заборонено");
}