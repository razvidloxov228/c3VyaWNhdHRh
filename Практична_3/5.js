let balance = Number(prompt("Ваш початковий баланс: "));
balance += 500;
console.log("Поповнено на 500 грн");
balance -= 200;
console.log("Знято 200 грн");
let bonus = balance*0.05;
balance += bonus;
console.log("Нараховано 5%: " + bonus + " грн");
console.log("Підсумковий баланс: " + balance + " грн");