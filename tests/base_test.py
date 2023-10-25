import unittest
from unittest.mock import patch
from scrapers import fetch_page


class BaseScraperTest(unittest.TestCase):

    def setUp(self):
        self.url = "https://example.com"
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        }

    def tearDown(self):
        pass

    @patch('requests.get')
    def test_fetch_page(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'<html>some content</html>'

        content = fetch_page(self.url, self.HEADERS)
        self.assertIsNotNone(content)
