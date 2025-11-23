import requests

def fetch_page(url: str):
    """Виконує GET-запит і повертає вміст сторінки."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Помилка: отримано статус-код {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Виникла помилка при виконанні запиту: {e}"

url = input("Введіть URL веб-ресурсу: ")

content = fetch_page(url)
print(content)
