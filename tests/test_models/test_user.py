import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.email = "test@test.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_attributes(self):
        self.assertEqual(self.user.email, "test@test.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()

