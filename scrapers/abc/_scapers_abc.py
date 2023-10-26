from __future__ import annotations

import typing as ty

from abc import ABC
from abc import abstractmethod
from bs4 import BeautifulSoup


class IScraper(ABC):
    @abstractmethod
    def get_soup(self) -> BeautifulSoup:
        pass

    @abstractmethod
    def process_soup(self, soup: BeautifulSoup) -> ty.List | ty.Dict[str, ty.Any]:
        pass

    @abstractmethod
    def scrape(self) -> ty.List | ty.Dict[str, ty.Any]:
        pass
