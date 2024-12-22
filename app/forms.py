# Проверено с сайтом Наставника

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm): # создаем форму регистрации
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=35)]) # указываем минимальное кол-во символов и максимальное кол-во символов
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) # указываем, что пароли должны совпадать
    submit = SubmitField('Sign Up') # создаем кнопку регистрации

    def validate_username(self, username): # создаем validate для поля username
        user = User.query.filter_by(username=username.data).first() # проверяем, есть ли пользователь с таким username
        if user: # если пользователь с таким username существует
            raise ValidationError('Такое имя пользователя уже существует') # выводим сообщение об ошибке

    def validate_email(self, email): # создаем validate для поля email
        user = User.query.filter_by(email=email.data).first() # проверяем, есть ли пользователь с таким email
        if user: # если пользователь с таким email
            raise ValidationError('Такой email уже существует') # выводим сообщение об ошибке


class LoginForm(FlaskForm): # создаем форму регистрации
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('login') # создаем кнопку регистрации