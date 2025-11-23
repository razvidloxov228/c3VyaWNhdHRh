import requests

def fetch_page(url: str, params: dict = None, filename: str = "output.html"):
    """Виконує GET-запит і зберігає вміст сторінки у файл."""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"[OK] Вміст сторінки успішно збережено у файл: {filename}")

        print("\n--- Заголовки відповіді ---")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

    except requests.exceptions.HTTPError as e:
        print(f"[X] HTTP-помилка: {e}")
    except requests.exceptions.ConnectionError:
        print("[X] Помилка з'єднання: сервер недоступний або немає інтернету")
    except requests.exceptions.Timeout:
        print("[X] Таймаут: сервер занадто довго відповідає")
    except requests.exceptions.RequestException as e:
        print(f"[X] Загальна помилка запиту: {e}")


if __name__ == "__main__":
    url = input("Введіть URL веб-ресурсу: ")
    filename = input("Введіть ім'я файлу для збереження (наприклад, page.html): ").strip()

    if not filename:
        filename = "output.html"

    fetch_page(url, filename=filename)
