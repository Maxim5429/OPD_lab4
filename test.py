import unittest # импортируем библиотеку для создания unit-тестов
from main import app # импортируем Flask-приложение, которое будем тестировать
class Test(unittest.TestCase): # создаем класс для тестирования
    def setUp(self): # вызываем метод для подготовки тестового устройства
        app.testing = True # установили значение True для тестирования
        self.app = app.test_client() # создаем клиент для тестирования
    def test_home(self): # тестируем страницу авторизации
        result = self.app.get('/') # отправляем GET-запрос на главную страницу
        self.assertEqual(result.status_code, 200) # проверяем, что код ответа равен 200
    def test_form(self): # тестируем кнопку
        result = self.app.get('/') # отправляем GET-запрос на главную страницу
        assert b"submit" in result.data # проверяем кнопку
    def test_false(self): # тестируем на ввод неверного логина и пароля
        test = app.test_client(self) # создаем клиент для тестирования
        response = test.post(data={'login':'maxim@google.com','password':'njnc78'}) # делаем POST-запрос,передаём неверные логин и пароль
        self.assertEqual('Неверный логин или пароль',response.text) # ответ, полученный в response должен быть равен 'Неверный логин или пароль'
    def test_true(self): # тестируем на ввод правильного логина и пароля
        test = app.test_client(self) # создаем клиент для тестирования
        with open('login.txt','r') as file: # открываем файл
            f=file.readlines() # получаем список строк из файла
        admin_login, admin_password = f[2].strip().split(":") # получаем правильные логин и пароль в переменные admin_login и admin_password
        response = test.post(data={'login':admin_login,'password':admin_password})  # делаем POST-запрос,передаём верные логин и пароль
        self.assertEqual('Вы зашли в свой профиль',response.text) # ответ, полученный в response должен быть равен 'Вы зашли в свой профиль'
    def test_register(self): # проверка того, что нельзя зарегистрироваться с уже существующим логином
        test = app.test_client(self)  # создаем клиент для тестирования
        response = test.post('/register',data={'login':'Artem20@yandex.ru','password': 'njnc78'})  # делаем POST-запрос,передаём уже существующий логин
        self.assertEqual('данный логин уже существует',response.text)  # ответ, полученный в response должен быть равен 'данный логин уже существует'
    def test_reg(self): # проверка регистрации
        test = app.test_client(self)  # создаем клиент для тестирования
        response = test.post('/register', data={'login': 'Evgeniy@gmail.com','password': 'rd65G7'})  # делаем POST-запрос,передаём логин и пароль для регистрации
        with open('login.txt', 'r') as file: # открываем файл
            line=file.readlines()[-1].strip() # считываем последнюю строку в line
        self.assertEqual("регистрация прошла успешно!",response.text) # ответ, полученный в response должен быть равен 'регистрация прошла успешно!'
        self.assertEqual(line,'Evgeniy@gmail.com:rd65G7')  # последняя строка из файла login.txt должна равняться 'Evgeniy@gmail.com:rd65G7'
if __name__ == '__main__': # при условии запуска скрипта
    unittest.main() # запускаем все тесты
