import requests

def fetch_page(url: str, params: dict = None):
    """Виконує GET-запит з параметрами та повертає вміст сторінки."""
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Вміст сторінки:\n")
            print(response.text)
        else:
            print(f"Помилка: отримано статус-код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка при виконанні запиту: {e}")

#url = "https://www.google.com/search"
#params = {"q": "Python requests"}
params = {}
url = input("Введіть URL веб-ресурсу: ")
add_params = input("Бажаєте додати параметри запиту? (так/ні): ").strip().lower()
if add_params == "так":
    while True:
        key = input("Введіть ім'я параметра (або Enter для завершення): ").strip()
        if not key:
            break
        value = input(f"Введіть значення для '{key}': ").strip()
        params[key] = value

fetch_page(url, params)
