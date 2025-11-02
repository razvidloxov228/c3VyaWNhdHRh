function Student(name, speciality, avrGrade, missedLessons) {
    this.name = name;
    this.speciality = speciality;
    this.avrGrade = avrGrade;
    this.missedLessons = missedLessons;

    this.printInfo = function() {
        console.log(`Ім'я: ${this.name}, Спеціальність: ${this.speciality}, Середній бал: ${this.avrGrade}, Кількість пропущених занять: ${this.missedLessons}`);
    };
}
const student1 = new Student("Олена", "Комп'ютерні технології", 91, 3);
const student2 = new Student("Іван", "Електрична інженерія", 85, 5);
const student3 = new Student("Марія", "Механічна інженерія", 95, 1);
student1.printInfo();
student2.printInfo();
student3.printInfo();
student1.printInfo.call(student2);
student2.printInfo.apply(student3);
const boundPrint = student3.printInfo.bind(student1);
boundPrint(); 