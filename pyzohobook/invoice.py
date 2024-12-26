import requests
import json


def create_invoice(
    invoice_data: dict, book_token: str, organization_id: str
) -> requests.Response:
    book_headers = {"Authorization": f"Zoho-oauthtoken {book_token}"}
    response = requests.post(
        f"https://www.zohoapis.ca/books/v3/invoices?organization_id={organization_id}",
        headers=book_headers,
        data=json.dumps(invoice_data),
    )
    return response


def update_invoice(
    invoice_id: str, invoice_data: dict, book_token: str, organization_id: str
) -> requests.Response:
    book_headers = {"Authorization": f"Zoho-oauthtoken {book_token}"}

    response = requests.put(
        f"https://www.zohoapis.ca/books/v3/invoices/{invoice_id}?organization_id={organization_id}",
        headers=book_headers,
        data=json.dumps(invoice_data),
    )

    return response


def delete_invoice(
    invoice_id: str, book_token: str, organization_id: str
) -> requests.Response:
    book_headers = {"Authorization": f"Zoho-oauthtoken {book_token}"}

    response = requests.delete(
        f"https://www.zohoapis.ca/books/v3/invoices/{invoice_id}?organization_id={organization_id}",
        headers=book_headers,
    )

    return response
