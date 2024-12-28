#pyzohobook/invoice.py
from .utils import *
import json
import requests

def create_invoice(
    invoice_data: dict, book_token: str, organization_id: str
) -> requests.Response:
    response = requests.post(
        f"https://www.zohoapis.ca/books/v3/invoices?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
        data=json.dumps(invoice_data),
    )
    return response


def update_invoice(
    invoice_id: str, invoice_data: dict, book_token: str, organization_id: str
) -> requests.Response:

    response = requests.put(
        f"https://www.zohoapis.ca/books/v3/invoices/{invoice_id}?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
        data=json.dumps(invoice_data),
    )

    return response


def delete_invoice(
    invoice_id: str, book_token: str, organization_id: str
) -> requests.Response:

    response = requests.delete(
        f"https://www.zohoapis.ca/books/v3/invoices/{invoice_id}?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
    )

    return response
