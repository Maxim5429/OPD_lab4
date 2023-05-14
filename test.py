import unittest
from main import app

class Test(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_log(self):
        test = app.test_client(self)
        response = test.post(data={'login':'maxim@google.com','password':'njnc78'})
        self.assertEqual('incorrect',response.text)





if __name__ == '__main__':
    unittest.main() #запускаем тесты
