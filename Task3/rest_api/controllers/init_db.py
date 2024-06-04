from pymongo import MongoClient

def init_db():
    client = MongoClient("mongodb", 27017)
    db = client["mydatabase"]

    # Создаем коллекцию users и добавляем тестовые данные
    users = db["users"]
    users.insert_many([
        {"username": "user1", "email": "user1@example.com", "password": "password1"},
        {"username": "user2", "email": "user2@example.com", "password": "password2"},
        {"username": "user3", "email": "user3@example.com", "password": "password3"},
    ])

