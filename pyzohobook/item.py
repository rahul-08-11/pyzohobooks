import requests
import json


def create_item(
    item_data: dict, book_token: str, organization_id: str
) -> requests.Response:
    book_headers = {"Authorization": f"Zoho-oauthtoken {book_token}"}
    response = requests.post(
        f"https://www.zohoapis.ca/books/v3/items?organization_id={organization_id}",
        headers=book_headers,
        data=json.dumps(item_data),
    )
    return response


def update_item(
    item_id: str, item_data: dict, book_token: str, organization_id: str
) -> requests.Response:
    book_headers = {"Authorization": f"Zoho-oauthtoken {book_token}"}

    response = requests.put(
        f"https://www.zohoapis.ca/books/v3/items/{item_id}?organization_id={organization_id}",
        headers=book_headers,
        data=json.dumps(item_data),
    )

    return response


def search_item(
    item_name: dict, book_token: str, organization_id: str
) -> requests.Response:
    book_headers = {"Authorization": f"Zoho-oauthtoken {book_token}"}

    response = requests.get(
        f"https://www.zohoapis.ca/books/v3/items?organization_id={organization_id}&name={item_name}",
        headers=book_headers,
    )

    return response


def delete_item(
    item_id: str, book_token: str, organization_id: str
) -> requests.Response:
    book_headers = {"Authorization": f"Zoho-oauthtoken {book_token}"}

    response = requests.delete(
        f"https://www.zohoapis.ca/books/v3/items/{item_id}?organization_id={organization_id}",
        headers=book_headers,
    )

    return response
