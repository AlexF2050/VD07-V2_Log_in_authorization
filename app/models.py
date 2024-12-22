# Проверено с сайтом Наставника

from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader # исполняет функцию для загрузки пользователя
def load_user(user_id): # функция для загрузки пользователя
    return User.query.get(int(user_id)) # получаем объект пользователя

# создание базы данных и модели пользователя
class User(db.Model, UserMixin): # создаем модель пользователя и колонки
    id = db.Column(db.Integer, primary_key=True) # id пользователя колонка
    username = db.Column(db.String(20), unique=True, nullable=False) # имя пользователя
    email = db.Column(db.String(120), unique=True, nullable=False) # email пользователя
    password = db.Column(db.String(60), nullable=False) # пароль пользователя

    def __repr__(self): # функция для вывода информации о пользователе
        return f"User('{self.username}', '{self.email}')" # возвращаем строку с информацией о пользователе

