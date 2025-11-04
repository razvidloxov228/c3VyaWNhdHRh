countries = {
    "Україна": "Київ",
    "Франція": "Париж",
    "Німеччина": "Берлін",
    "Італія": "Рим",
    "Японія": "Токіо"
}
while True:
    country = input("Введіть назву країни (або 'вихід' для завершення): ")

    if country.lower() == "вихід":
        print("Програму завершено.")
        break

    if country in countries:
        print(f"Столиця країни {country} — {countries[country]}")
    else:
        print("На жаль, інформації про цю країну немає у словнику.")
