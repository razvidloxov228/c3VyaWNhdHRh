let daynum = Number(prompt("Введіть число(1-7): "));
let day;
switch (daynum) {
    case 1:
        day = "понеділок";
        break;
    case 2:
        day = "вівторок";
        break;
    case 3:
        day = "середа";
        break;
    case 4:
        day = "четвер";
        break;
    case 5:
        day = "п'ятниця";
        break;
    case 6:
        day = "субота";
        break;
    case 7:
        day = "неділя";
        break;
    default:
        day = "значення неправильне. 1-7!";
}
console.log("Це " + day);
