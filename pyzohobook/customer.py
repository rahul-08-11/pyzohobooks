# pyzohobook/customer.py
from .helpers import *
import json
import requests
from urllib.parse import urlencode
from .config import Config
from typing import Literal


class Customer:
    """
    A class representing a customer, providing methods to search for customers.

    Attributes:
        config (Config): An instance of the Config class, used to store configuration settings.
    """

    config = Config()

    @classmethod
    def search_customer(cls, search_params: dict, book_token: str) -> requests.Response:
        """
        Searches for a customer based on the provided search parameters.

        Args:
            search_params (dict): A dictionary containing search parameters.
            book_token (str): A token used for authentication.

        Returns:
            requests.Response: The response from the API search request.

        Note:
            The search parameters are encoded into the query string and appended to the API URL.
        """
        # Encode search parameters into the query string
        query_string = urlencode(search_params)
        response = requests.get(
            f"{cls.config.domain_url}/contacts?organization_id={cls.config.organization_id}&{query_string}",
            headers=get_book_headers(book_token=book_token),
        )
        return response  # return first account
