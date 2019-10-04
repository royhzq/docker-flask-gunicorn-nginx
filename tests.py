import os
import unittest
from app import app

class APITests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_api(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
 
if __name__ == "__main__":
    unittest.main()