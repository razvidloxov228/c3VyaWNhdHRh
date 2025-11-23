import requests

def fetch_page(url: str, params: dict = None):
    """Виконує GET-запит і виводить заголовки та вміст сторінки."""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        print("[OK] Запит виконано успішно")

        print("\n--- Заголовки відповіді ---")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print("\n--- Вміст сторінки ---")
        print(response.text[:300])

    except requests.exceptions.HTTPError as e:
        print(f"[X] HTTP-помилка: {e}")
    except requests.exceptions.ConnectionError:
        print("[X] Помилка з'єднання: сервер недоступний або немає інтернету")
    except requests.exceptions.Timeout:
        print("[X] Таймаут: сервер занадто довго відповідає")
    except requests.exceptions.RequestException as e:
        print(f"[X] Загальна помилка запиту: {e}")


def send_post_request(url: str, data: dict):
    """Виконує POST-запит і виводить відповідь сервера."""
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        print("[OK] POST-запит виконано успішно")

        print("\n--- Відповідь сервера ---")
        print(response.text[:300])
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
    choice = input("Виконати GET чи POST? (get/post): ").strip().lower()

    if choice == "get":
        fetch_page(url)
    elif choice == "post":
        username = input("Введіть ім'я користувача: ")
        password = input("Введіть пароль: ")
        payload = {"username": username, "password": password}
        send_post_request(url, payload)
    else:
        print("[X] Невідомий тип запиту")
