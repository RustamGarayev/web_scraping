import responses
from bs4 import BeautifulSoup

from tests.base_test import BaseScraperTest
from scrapers import BinaAzScraper


class BinaAzScraperTest(BaseScraperTest):
    def setUp(self) -> None:
        super().setUp()
        self.url = "https://bina.az/alqi-satqi?page=1"
        self.scraper = BinaAzScraper(self.url, self.HEADERS)

    @responses.activate
    def test_get_soup(self):
        responses.add(responses.GET, self.url, body="<html></html>", status=200)

        soup = self.scraper.get_soup()

        assert isinstance(soup, BeautifulSoup)
        assert soup.find("html") is not None

    def test_process_soup(self):
        soup = BeautifulSoup(
            '<html><div class="items_list">...</div></html>', "html.parser"
        )

        # Assuming that process_soup should return a list of House objects
        result = self.scraper.process_soup(soup)

        assert isinstance(result, list)
        # ... will be updated ...

    @responses.activate
    def test_scrape(self):
        # Mock the response
        responses.add(
            responses.GET,
            self.url,
            body="<html><div class='items_list'>...</div></html>",
            status=200,
        )

        result = self.scraper.scrape()

        assert isinstance(result, list)
        # ... will be updated ...
