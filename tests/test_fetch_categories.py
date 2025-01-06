import unittest
from unittest.mock import patch
from scripts.fetch_categories import fetch_categories

class TestFetchCategories(unittest.TestCase):

    @patch('scripts.fetch_categories.requests.get')
    def test_fetch_categories(self, mock_get):
        mock_get.return_value.content = """
        <html>
            <body>
                <a href="/sindresorhus/awesome">Awesome List</a>
                <a href="/sindresorhus/awesome-nodejs">Awesome Node.js</a>
            </body>
        </html>
        """
        categories = fetch_categories()
        self.assertIn('/sindresorhus/awesome', categories)
        self.assertIn('/sindresorhus/awesome-nodejs', categories)

if __name__ == '__main__':
    unittest.main()
