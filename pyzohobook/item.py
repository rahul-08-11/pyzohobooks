# pyzohobook/item.py
from .helpers import *
import json
import requests
from urllib.parse import urlencode
from .config import Config
from typing import Literal


class Item:
    """
    A class representing an item, providing methods for creating, updating, searching, and deleting items.
    """

    config = Config()

    @classmethod
    def create_item(
        cls, item_data: dict, book_token: str, organization_id: str
    ) -> requests.Response:
        """
        Creates a new item.

        Args:
            item_data (dict): The data for the new item.
            book_token (str): The book token for authentication.
            organization_id (str): The ID of the organization.

        Returns:
            requests.Response: The response from the API.
        """
        response = requests.post(
            f"{cls.config.domain_url}/items?organization_id={cls.config.organization_id}",
            headers=get_book_headers(book_token=book_token),
            data=json.dumps(item_data),
        )
        return response

    @classmethod
    def update_item(
        cls, item_id: str, item_data: dict, book_token: str
    ) -> requests.Response:
        """
        Updates an existing item.

        Args:
            item_id (str): The ID of the item to update.
            item_data (dict): The updated data for the item.
            book_token (str): The book token for authentication.

        Returns:
            requests.Response: The response from the API.
        """
        response = requests.put(
            f"{cls.config.domain_url}/items/{item_id}?organization_id={cls.config.organization_id}",
            headers=get_book_headers(book_token=book_token),
            data=json.dumps(item_data),
        )
        return response

    @classmethod
    def search_item(
        cls, item_name: dict, book_token: str, organization_id: str
    ) -> requests.Response:
        """
        Searches for an item by name.

        Args:
            item_name (dict): The name of the item to search for.
            book_token (str): The book token for authentication.
            organization_id (str): The ID of the organization.

        Returns:
            requests.Response: The response from the API.
        """
        response = requests.get(
            f"{cls.config.domain_url}/items?organization_id={cls.config.organization_id}&name={item_name}",
            headers=get_book_headers(book_token=book_token),
        )
        return response

    @classmethod
    def delete_item(
        cls, item_id: str, book_token: str, organization_id: str
    ) -> requests.Response:
        """
        Deletes an item.

        Args:
            item_id (str): The ID of the item to delete.
            book_token (str): The book token for authentication.
            organization_id (str): The ID of the organization.

        Returns:
            requests.Response: The response from the API.
        """
        response = requests.delete(
            f"{cls.config.domain_url}/items/{item_id}?organization_id={cls.config.organization_id}",
            headers=get_book_headers(book_token=book_token),
        )
        return response
