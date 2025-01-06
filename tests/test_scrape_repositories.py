import unittest
from unittest.mock import patch
from scripts.scrape_repositories import scrape_repositories

class TestScrapeRepositories(unittest.TestCase):

    @patch('scripts.scrape_repositories.requests.get')
    def test_scrape_repositories(self, mock_get):
        mock_get.return_value.content = """
        <html>
            <body>
                <a href="/user/repo1">Repo 1</a>
                <a href="/user/repo2">Repo 2</a>
            </body>
        </html>
        """
        repositories = scrape_repositories('/dummy-category')
        self.assertIn('https://github.com/user/repo1', repositories)
        self.assertIn('https://github.com/user/repo2', repositories)

if __name__ == '__main__':
    unittest.main()
