import requests
import json
from urllib.parse import urlencode

def search_customer(search_params : dict, book_token : str, organization_id : str) -> requests.Response:
    book_headers = {
        "Authorization": f"Zoho-oauthtoken {book_token}"
    }
    # Encode search parameters into the query string
    query_string = urlencode(search_params)
    contact_response = requests.get(
        f"https://www.zohoapis.ca/books/v3/contacts?organization_id={organization_id}&zcrm_account_id={customer_id}",
        headers=book_headers,
    )
    return contact_response  # return first account


