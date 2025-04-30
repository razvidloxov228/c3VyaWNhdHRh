class Abonent {
    constructor(name, number) {
        this.name = name;
        this.number = number;
    }
    get getAbonent() {
        return `Ім'я: ${this.name}, Номер: ${this.number}`;
    }
}
class PhoneBook {
    constructor() {
        this.contacts = [];
    }
    addContact(name, number) {
        const newContact = new Abonent(name, number);
        this.contacts.push(newContact);
    }
    showContacts() {
        console.log("Контакти: ");
        this.contacts.forEach(contact => console.log(contact.getAbonent));
        }
    }
const phoneBook = new PhoneBook();
phoneBook.addContact("ДСНС", 101);
phoneBook.addContact("Поліція", 102);
phoneBook.addContact("Швидка", 103);
function main() {
    while (true) {
        const action = prompt("Виберіть дію ('додати', 'показати', 'вийти'): ").toLowerCase();

        if (action === "додати") {
            const name = prompt("Введіть ім'я: ");
            const number = prompt("Введіть номер: ");
            phoneBook.addContact(name, number);
            console.log(`Абонента ${name} додано.`);
        } else if (action === "показати") {
            phoneBook.showContacts();
        } else if (action === "вийти") {
            console.log("Вихід із програми.");
            break;
        } else {
            console.log("Спробуйте ще раз.");
        }
    }
}
main();