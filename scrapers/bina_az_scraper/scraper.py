import requests
import typing as ty

from bs4 import BeautifulSoup
from scrapers import fetch_page


class BinaAzScraper:
    def __init__(self, url: str, headers: ty.Dict[str, str]):
        self.__url = url
        self.__headers = headers
