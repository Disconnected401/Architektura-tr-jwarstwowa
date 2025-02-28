import unittest
import json
from controllers.user_controller import app

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users', data=json.dumps({
            'firstName': 'John',
            'lastName': 'Doe',
            'birthYear': 1990,
            'group': 'user'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):
        response = self.app.post('/users', data=json.dumps({
            'firstName': 'John',
            'lastName': 'Doe',
            'birthYear': 1990,
            'group': 'user'
        }), content_type='application/json')
        user_id = json.loads(response.data)['id']
        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.app.post('/users', data=json.dumps({
            'firstName': 'John',
            'lastName': 'Doe',
            'birthYear': 1990,
            'group': 'user'
        }), content_type='application/json')
        user_id = json.loads(response.data)['id']
        response = self.app.patch(f'/users/{user_id}', data=json.dumps({
            'firstName': 'Jane',
            'lastName': 'Doe',
            'birthYear': 1991,
            'group': 'premium'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        response = self.app.post('/users', data=json.dumps({
            'firstName': 'John',
            'lastName': 'Doe',
            'birthYear': 1990,
            'group': 'user'
        }), content_type='application/json')
        user_id = json.loads(response.data)['id']
        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
