# Create an invoice in Zoho Books
import json
import requests


# Create a bill in Zoho Books
def create_bill(bill_data : dict, book_token : str, organization_id : str) -> requests.Response:
    book_headers = {
        "Authorization": f"Zoho-oauthtoken {book_token}"
    }
    response = requests.post(
        f"https://www.zohoapis.ca/books/v3/bills?organization_id={organization_id}",
        headers=book_headers,
        data=json.dumps(bill_data)
    )
    return response


def delete_bill(bill_id : str, book_token : str, organization_id : str) -> requests.Response:
    book_headers = {
        "Authorization": f"Zoho-oauthtoken {book_token}"
    }
    response = requests.delete(
        f"https://www.zohoapis.ca/books/v3/bills/{bill_id}?organization_id={organization_id}",
        headers=book_headers
    )

    return response


def update_bill(bill_id : str, bill_data : dict, book_token : str, organization_id : str) -> requests.Response:

    book_headers = {
        "Authorization": f"Zoho-oauthtoken {book_token}"
    }

    response = requests.put(
        f"https://www.zohoapis.ca/books/v3/bills/{bill_id}?organization_id={organization_id}",
        headers=book_headers,
        data=json.dumps(bill_data)
    )

    return response