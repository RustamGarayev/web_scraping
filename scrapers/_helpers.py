import requests
import typing as ty


def fetch_page(url: str, headers: ty.Dict) -> ty.Union[requests.Response, ty.Dict[str, ty.Any]]:
    try:
        return requests.get(url, headers=headers)
    except requests.RequestException as e:
        return {
            "status": 500,
            "message": f"Something went wrong\nPossible cause: {e}",
            "body": None
        }
