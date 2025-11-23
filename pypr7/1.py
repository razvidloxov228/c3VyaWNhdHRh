class User:
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def create_user(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        print(f"Користувача '{self.name}' створено.")

    def update_user(self, name=None, email=None, password=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if password:
            self.password = password
        print(f"Дані користувача '{self.name}' оновлено.")

    def delete_user(self):
        print(f"Користувача '{self.name}' видалено.")
        self.name = None
        self.email = None
        self.password = None


user1 = User()

user1.create_user("Вадим", "razvidloxov228@freemail.com", "nelomayemiy228")

user1.update_user(email="razvidloxov229@email.com")

user1.delete_user()
