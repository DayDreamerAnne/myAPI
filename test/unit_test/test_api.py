import unittest
from app import app
class WatchlistTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(
            TESTING=True
        )

        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertIn('Page Not Found - 404', data)
        self.assertIn('Go Back', data)
        self.assertEqual(response.status_code, 404)


    def test_home_page (self):
        response = self.client.get('/employees')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()