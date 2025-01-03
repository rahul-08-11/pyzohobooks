# pyzohobook/invoice.py
from .utils import *
import json
import requests
from urllib.parse import urlencode
from .config import Config
from typing import Literal


class Invoice:
    """
    A class for managing invoices in Zoho Books.

    Attributes:
        config (Config): Configuration object for Zoho Books API.

    Methods:
        create_invoice: Creates a new invoice in Zoho Books.
        update_invoice: Updates an existing invoice in Zoho Books.
        delete_invoice: Deletes an invoice in Zoho Books by its ID.
        search_invoice: Searches for invoices in Zoho Books.
        mark_invoice: Marks an invoice with a specified status in Zoho Books.
        fetch_invoice: Fetches an invoice in Zoho Books.
    """

    config = Config()

    @classmethod
    def create_invoice(cls, invoice_data: dict, book_token: str) -> requests.Response:
        """
        Creates an invoice in Zoho Books.

        Args:
            invoice_data (dict): Data for the new invoice.
            book_token (str): Zoho Books API token.
            organization_id (str): Organization ID in Zoho Books.

        Returns:
            requests.Response: Response object containing the ID of the newly created invoice.
        """
        response = requests.post(
            f"{cls.config.domain_url}/invoices?organization_id={cls.config.organization_id}",
            headers=get_book_headers(book_token=book_token),
            data=json.dumps(invoice_data),
        )
        return response

    def update_invoice(
        cls, invoice_id: str, invoice_data: dict, book_token: str
    ) -> requests.Response:
        """
        Updates an invoice in Zoho Books.

        Args:
            invoice_id (str): The ID of the invoice to be updated.
            invoice_data (dict): The data to update the invoice with.
            book_token (str): Zoho Books API token.
            organization_id (str): Organization ID in Zoho Books.

        Returns:
            requests.Response: Response object containing the result of the update operation.
        """

        response = requests.put(
            f"{cls.config.domain_url}/invoices/{invoice_id}?organization_id={cls.config.organization_id}",
            headers=get_book_headers(book_token=book_token),
            data=json.dumps(invoice_data),
        )

        return response

    @classmethod
    def delete_invoice(
        cls, invoice_id: str, book_token: str, organization_id: str
    ) -> requests.Response:
        """
        Deletes an invoice in Zoho Books.

        Args:
            invoice_id (str): The ID of the invoice to be deleted.
            book_token (str): Zoho Books API token.
            organization_id (str): Organization ID in Zoho Books.

        Returns:
            requests.Response: Response object containing the result of the delete operation.
        """
        response = requests.delete(
            f"{cls.config.domain_url}/invoices/{invoice_id}?organization_id={cls.config.organization_id}",
            headers=get_book_headers(book_token=book_token),
        )

        return response

    @classmethod
    def search_invoice(cls, search_params: dict, book_token: str) -> requests.Response:

        # Encode search parameters into the query string

        """
        Searches for invoices in Zoho Books.

        Args:
            search_params (dict): Dictionary of search parameters.
            book_token (str): Zoho Books API token.
            organization_id (str): Organization ID in Zoho Books.

        Returns:
            requests.Response: Response object containing the search results.

        Supported search parameters:
            - invoice_number (str): Search invoices by invoice number.
            - customer_name (str): Search invoices by customer name.
            - invoice_status (str): Search invoices by invoice status.
            - invoice_date (str): Search invoices by invoice date.
            - due_date (str): Search invoices by due date.
            - total (str): Search invoices by total amount.
            - page (int): Page number to retrieve.
            - per_page (int): Number of records to retrieve per page.

        Note:
            - The search parameters are case-sensitive.
        """
        query_string = urlencode(search_params)
        response = requests.get(
            f"{cls.config.domain_url}/invoices?organization_id={cls.config.organization_id}&{query_string}",
            headers=get_book_headers(book_token=book_token),
        )

        return response

    @classmethod
    def mark_invoice(
        cls, book_token: str, invoice_id: str, status: Literal["sent", "draft", "void"]
    ) -> requests.Response:
        """
        Marks an invoice with a specified status in Zoho Books.

        Args:
            book_token (str): Zoho Books API token.
            invoice_id (str): The ID of the invoice to be marked.
            organization_id (str): Organization ID in Zoho Books.
            status (Literal['sent','draft','void']): The status to mark the invoice with.

        Returns:
            requests.Response: Response object containing the result of the mark operation.

        Raises:
            requests.exceptions.RequestException: If the request to the Zoho Books API fails.
        """

        response = requests.post(
            f"{cls.config.domain_url}/invoices/{invoice_id}/status/{status}?organization_id={cls.config.organization_id}",
            headers=get_book_headers(book_token=book_token),
        )

        return response

    @classmethod
    def fetch_invoice(
        cls, invoice_id: str, book_token: str, formate: Literal["pdf", "json", "html"]
    ) -> requests.Response:
        """
        Fetches an invoice in Zoho Books.

        Args:
            invoice_id (str): The ID of the invoice to be fetched.
            book_token (str): Zoho Books API token.
            organization_id (str): Organization ID in Zoho Books.
            formate (Literal['pdf','json','html']): The format of the invoice to be fetched.

        Returns:
            requests.Response: Response object containing the invoice in the specified format.

        Raises:
            requests.exceptions.RequestException: If the request to the Zoho Books API fails.
        """
        response = requests.get(
            f"{cls.config.domain_url}/invoices/{formate}?organization_id={cls.config.organization_id}&invoice_ids={invoice_id}",
            headers=get_book_headers(book_token=book_token),
        )

        return response
