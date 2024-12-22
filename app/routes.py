# Проверено с сайтом Наставника

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, EditProfileForm
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') # шифрование пароля
        user = User(username=form.username.data, email=form.email.data, password=hashed_password) # добавление пользователя
        db.session.add(user) # добавление пользователя в базу данных
        db.session.commit() # запись в базу данных
        flash('Вы успешно зарегистрировались!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Введены неверные данные')
    return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html')

# Домашнее задание

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data # юзеру присваивается имя
        current_user.email = form.email.data # юзеру присваивается email
        current_user.password = form.password.data # юзеру присваивается пароль
        db.session.commit() # запись в базу данных
        flash('Ваш профиль был обновлен!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET': # юзеру присваивается имя
        form.username.data = current_user.username # юзеру присваивается имя
        form.email.data = current_user.email #
        form.password.data = current_user.password #
    return render_template('edit_profile.html', form=form)