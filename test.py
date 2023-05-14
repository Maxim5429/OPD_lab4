import unittest
from main import app
class Test(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200) #проверяем, что код ответа равен 200
    def test_form(self):
        result = self.app.get('/')
        assert b"submit" in result.data #проверяем кнопку

    def test_false(self):
        test = app.test_client(self)
        response = test.post(data={'login':'maxim@google.com','password':'njnc78'})
        self.assertEqual('incorrect',response.text) #вводим неверный логин и пароль, проверяем результат
    def test_true(self):
        test = app.test_client(self)
        with open('login.txt','r') as file:
            f=file.readlines()
        admin_login = f[0].strip()
        admin_password = f[1].strip()
        response = test.post(data={'login':admin_login,'password':admin_password})
        self.assertEqual('correct',response.text) #вводим правильный логин и пароль, проверяем результат

if __name__ == '__main__':
    unittest.main() #запускаем тесты
