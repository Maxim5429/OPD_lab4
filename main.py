from flask import Flask, render_template, request

app = Flask(__name__) #создание объекта класса Flask

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/', methods=['post', 'get']) # вход
def form():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        with open('login.txt', 'r') as f:
            for line in f:
                admin_login, admin_password = line.strip().split(":")
                if (login==admin_login) and (password==admin_password):
                    return("Вы зашли в свой профиль")
            else:
                return("Неверный логин или пароль")
@app.route('/register')
def register():
    return render_template("registration.html")
@app.route('/register', methods=['post', 'get']) # регистрация
def reg():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        with open('login.txt', 'r') as file:   # проверка, занят ли данный логин
            for line in file:
                admin_login, admin_password = line.strip().split(":")
                if login==admin_login:
                    return "данный логин уже существует"
        with open('login.txt','a+') as file:
            file.write(f"{login}:{password}\n")
            return "регистрация прошла успешно!"
if __name__ == '__main__': #запуск
    app.run(debug=True)