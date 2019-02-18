import unittest
from app.models import User

class UserModel(unittest.TestCase):

    def setup(self):
        self.new_user = User(password="anum123")

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('anum123'))