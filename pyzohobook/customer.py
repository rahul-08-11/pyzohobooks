#pyzohobook/customer.py
from .utils import *
import requests
import json 
from urllib.parse import urlencode

def search_customer(
    search_params: dict, book_token: str, organization_id: str
) -> requests.Response:
    # Encode search parameters into the query string
    query_string = urlencode(search_params)
    response = requests.get(
        f"https://www.zohoapis.ca/books/v3/contacts?organization_id={organization_id}&{query_string}",
        headers=get_book_headers(book_token=book_token),
    )
    return response  # return first account
