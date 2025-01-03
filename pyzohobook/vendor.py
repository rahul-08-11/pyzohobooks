# pyzohobook/vendor.py

from .utils import *
import json
import requests
from urllib.parse import urlencode
from . import config
from typing import Literal


class Vendor:
    """
    Provides methods for interacting with the Zoho Books API.

    The `Vendor` class provides methods for searching vendors and retrieving their details.
    It uses the `Config` class to store configuration values such as the domain URL and organization ID.

    Attributes:
        config (Config): Configuration object containing domain URL and organization ID.

    Methods:
        search_vendor(search_params: dict, book_token: str) -> requests.Response:
            Searches for vendors using the Zoho Books API.
    """

    config = config.Config()

    @classmethod
    def search_vendor(cls, search_params: dict, book_token: str) -> requests.Response:
        """
        Searches for vendors using the Zoho Books API.

        Args:
            search_params (dict): Search parameters for vendor.
            book_token (str): Zoho Books API token.

        Returns:
            requests.Response: Response object containing vendor details.

        Note:
            The organization_id is retrieved from the config object.
        """
        # Encode search parameters into the query string
        query_string = urlencode(search_params)
        vendor_response = requests.get(
            f"{cls.config.domain_url}/vendors?organization_id={cls.config.organization_id}&{query_string}",
            headers=get_book_headers(book_token=book_token),
        )
        return vendor_response
