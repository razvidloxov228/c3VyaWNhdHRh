import requests

def fetch_page(url: str, params: dict = None):
    """Виконує GET-запит і виводить заголовки та вміст сторінки."""
    try:
        response = requests.get(url, params=params)

        print("Заголовки відповіді:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print("\n--- Статус-код ---")
        print(response.status_code)

        print("\n--- Вміст сторінки ---")
        print(response.text[:500])

    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка при виконанні запиту: {e}")

url = input("Введіть URL веб-ресурсу: ")
fetch_page(url)
