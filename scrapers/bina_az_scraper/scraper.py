import typing as ty


class BinaAzScraper:
    def __init__(self, url: str, headers: ty.Dict[str, str]):
        self.__url = url
        self.__headers = headers
