import requests
import json
from urllib.parse import urlencode

# Fetch vendor details
def search_vendor(search_params : dict, book_token : str, organization_id : str) -> requests.Response:
    book_headers = {
        "Authorization": f"Zoho-oauthtoken {book_token}"
    }
    # Encode search parameters into the query string
    query_string = urlencode(search_params)
    vendor_response = requests.get(
        f"https://www.zohoapis.ca/books/v3/vendors?organization_id={organization_id}&vendor_name={vendor_name}",
        headers=book_headers,
    )
    return vendor_response # return first vendor