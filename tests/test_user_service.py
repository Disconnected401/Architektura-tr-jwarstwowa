import unittest
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService()

    def test_create_user(self):
        user_id = self.user_service.create_user('John', 'Doe', 1990, 'user')
        self.assertIsNotNone(user_id)

    def test_get_user(self):
        user_id = self.user_service.create_user('John', 'Doe', 1990, 'user')
        user = self.user_service.get_user(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, 'John')

    def test_update_user(self):
        user_id = self.user_service.create_user('John', 'Doe', 1990, 'user')
        updated = self.user_service.update_user(user_id, 'Jane', 'Doe', 1991, 'premium')
        self.assertTrue(updated)
        user = self.user_service.get_user(user_id)
        self.assertEqual(user.first_name, 'Jane')

    def test_delete_user(self):
        user_id = self.user_service.create_user('John', 'Doe', 1990, 'user')
        deleted = self.user_service.delete_user(user_id)
        self.assertTrue(deleted)
        user = self.user_service.get_user(user_id)
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
