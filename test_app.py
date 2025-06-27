import unittest
import json
from api import app

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        response = self.app.post('/users', data=json.dumps({
            "name": "Test User",
            "email": "test@example.com"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_update_user(self):
        self.app.post('/users', data=json.dumps({
            "name": "Temp User",
            "email": "temp@example.com"
        }), content_type='application/json')
        response = self.app.put('/users/1', data=json.dumps({
            "name": "Updated User",
            "email": "updated@example.com"
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        self.app.post('/users', data=json.dumps({
            "name": "Delete User",
            "email": "delete@example.com"
        }), content_type='application/json')
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
