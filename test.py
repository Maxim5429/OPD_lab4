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
        self.assertEqual('incorrect',response.text) # ответ, полученный в response должен быть равен 'incorrect'
    def test_true(self): # тестируем на ввод правильного логина и пароля
        test = app.test_client(self) # создаем клиент для тестирования
        with open('login.txt','r') as file: # открываем файл
            f=file.readlines() # получаем список строк из файла
        admin_login = f[0].strip() # присваиваем admin_login 1-ую строку, удаляем пробелы
        admin_password = f[1].strip() # присваиваем admin_password 2-ую строку, удаляем пробелы
        response = test.post(data={'login':admin_login,'password':admin_password})  # делаем POST-запрос,передаём верные логин и пароль
        self.assertEqual('correct',response.text) # ответ, полученный в response должен быть равен 'correct'

if __name__ == '__main__': # при условии запуска скрипта
    unittest.main() # запускаем все тесты
