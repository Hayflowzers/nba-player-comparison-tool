import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'NBA Player Comparison', response.data)

    def test_player_form(self):
        response = self.app.get('/player')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search for Player Stats', response.data)

    def test_compare_form(self):
        response = self.app.get('/compare')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Compare Player Stats', response.data)

if __name__ == '__main__':
    unittest.main()
