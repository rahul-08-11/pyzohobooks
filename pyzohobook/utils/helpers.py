# utils/helpers.py
import json
import requests
from urllib.parse import urlencode
from pyzohobook.config import Config
from typing import Literal


def get_book_headers(book_token: str) -> dict:
    """
    Generates the authorization headers for Zoho Books API.

    Args:
        book_token (str): The Zoho Books token.

    Returns:
        dict: Headers with the authorization token.
    """
    return {"Authorization": f"Zoho-oauthtoken {book_token}"}
