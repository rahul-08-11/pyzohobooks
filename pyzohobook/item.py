#pyzohobook/item.py
from .utils import *
import json
import requests


def create_item(
    item_data: dict, book_token: str, organization_id: str
) -> requests.Response:
    response = requests.post(
        f"https://www.zohoapis.ca/books/v3/items?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
        data=json.dumps(item_data),
    )
    return response


def update_item(
    item_id: str, item_data: dict, book_token: str, organization_id: str
) -> requests.Response:

    response = requests.put(
        f"https://www.zohoapis.ca/books/v3/items/{item_id}?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
        data=json.dumps(item_data),
    )

    return response


def search_item(
    item_name: dict, book_token: str, organization_id: str
) -> requests.Response:

    response = requests.get(
        f"https://www.zohoapis.ca/books/v3/items?organization_id={organization_id}&name={item_name}",
        headers=get_book_headers(book_token=book_token),
    )

    return response


def delete_item(
    item_id: str, book_token: str, organization_id: str
) -> requests.Response:

    response = requests.delete(
        f"https://www.zohoapis.ca/books/v3/items/{item_id}?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
    )

    return response
