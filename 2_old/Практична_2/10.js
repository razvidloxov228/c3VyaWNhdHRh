let object = {};
object.name = "Кирило";
object.age = 33;
object.city = "Моріо";
delete object.city;
object.likeCats = true;
for (let key in object) {
  console.log(key + ": " + object[key]);
}
