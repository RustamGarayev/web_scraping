import requests
import typing as ty

from bs4 import BeautifulSoup


def fetch_page(
    url: str, headers: ty.Dict[str, str]
) -> ty.Union[requests.Response, ty.Dict[str, ty.Any]]:
    try:
        return requests.get(url, headers=headers)
    except requests.RequestException as e:
        return {
            "status": 500,
            "message": f"Something went wrong\nPossible cause: {e}",
            "body": None,
        }


def form_soup(
    response: requests.Response,
    parser: ty.Literal["html.parser", "lxml"] = "html.parser",
):
    return BeautifulSoup(response.content, parser)
