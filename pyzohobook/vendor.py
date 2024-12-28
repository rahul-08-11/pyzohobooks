#pyzohobook/vendor.py

from .utils import *
import json
import requests
from urllib.parse import urlencode

# Fetch vendor details
def search_vendor(
    search_params: dict, book_token: str, organization_id: str
) -> requests.Response:
    """
    
    Args:
        search_params (dict): Search parameters for vendor.
        book_token (str): Zoho Books API token.
        organization_id (str): Organization ID in Zoho Books.

    Returns:
        requests.Response: Response object containing vendor details.
    """
    # Encode search parameters into the query string
    query_string = urlencode(search_params)
    vendor_response = requests.get(
        f"https://www.zohoapis.ca/books/v3/vendors?organization_id={organization_id}&{query_string}",
        headers=get_book_headers(book_token=book_token),
    )
    return vendor_response  
