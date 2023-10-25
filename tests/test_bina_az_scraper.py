from .base_test import BaseScraperTest


class BinaAzScraperTest(BaseScraperTest):
    def setUp(self) -> None:
        super().setUp()
        self.url = "https://bina.az/alqi-satqi?page=1"
