# pyzohobook/bill.py
from .utils.helpers import *


class Bill:
    """
    A class to manage bill operations in Zoho Books.

    This class provides methods to create, delete, and update bills using the Zoho Books API.
    All operations use the shared `Config` instance for configuration values.
    """

    # Shared Config instance for accessing configuration details
    config = Config()

    @classmethod
    def create_bill(cls, bill_data: dict, book_token: str) -> requests.Response:
        """
        Creates a new bill in Zoho Books.

        Args:
            bill_data (dict): A dictionary containing the bill data to be created.
            book_token (str): Zoho Books API token.

        Returns:
            requests.Response: The response object from the API call, including the newly created bill's details.
        """
        url = f"{cls.config.domain_url}/bills?organization_id={cls.config.organization_id}"
        headers = get_book_headers(book_token=book_token)

        # Make the POST request to create a new bill
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(bill_data),
        )
        return response

    @classmethod
    def delete_bill(cls, bill_id: str, book_token: str) -> requests.Response:
        """
        Deletes an existing bill in Zoho Books.

        Args:
            bill_id (str): The unique identifier of the bill to delete.
            book_token (str): Zoho Books API token.

        Returns:
            requests.Response: The response object from the API call, including the result of the delete operation.
        """
        url = f"{cls.config.domain_url}/bills/{bill_id}?organization_id={cls.config.organization_id}"
        headers = get_book_headers(book_token=book_token)

        # Make the DELETE request to remove the bill
        response = requests.delete(url, headers=headers)
        return response

    @classmethod
    def update_bill(cls, bill_id: str, bill_data: dict, book_token: str) -> requests.Response:
        """
        Updates an existing bill in Zoho Books.

        Args:
            bill_id (str): The unique identifier of the bill to update.
            bill_data (dict): A dictionary containing the updated bill data.
            book_token (str): Zoho Books API token.

        Returns:
            requests.Response: The response object from the API call, including the result of the update operation.
        """
        url = f"{cls.config.domain_url}/bills/{bill_id}?organization_id={cls.config.organization_id}"
        headers = get_book_headers(book_token=book_token)

        # Make the PUT request to update the bill
        response = requests.put(
            url,
            headers=headers,
            data=json.dumps(bill_data),
        )
        return response