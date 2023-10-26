import typing as ty

from scrapers.abc import IScraper

from scrapers import fetch_page
from scrapers import form_soup


class BinaAzScraper(IScraper):
    def __init__(self, url: str, headers: ty.Dict[str, str]):
        self.__url = url
        self.__headers = headers

    def get_soup(self):
        response = fetch_page(self.__url, headers=self.__headers)
        if response.status_code == 200:
            return form_soup(response)
        return None

    def process_soup(self, soup):
        list_of_houses = []
        # ... logic is to be implemented ...
        return list_of_houses

    def scrape(self):
        soup = self.get_soup()
        if soup:
            return self.process_soup(soup)
        return []
