import requests

def send_post_request(url: str, data: dict):
    """Виконує POST-запит з переданими даними."""
    try:
        response = requests.post(url, data=data)

        # Перевірка статусу відповіді
        if response.status_code == 200:
            print("Відповідь сервера:\n")
            print(response.text)
        else:
            print(f"Помилка: отримано статус-код {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Виникла помилка при виконанні запиту: {e}")

url = input("Введіть URL веб-ресурсу: ")

username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

payload = {
    "username": username,
    "password": password
}

send_post_request(url, payload)
