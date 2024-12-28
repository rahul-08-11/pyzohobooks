#pyzohobook/bill.py
from utils import *

# Create a bill in Zoho Books
def create_bill(
    bill_data: dict, book_token: str, organization_id: str
) -> requests.Response:
    response = requests.post(
        f"https://www.zohoapis.ca/books/v3/bills?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
        data=json.dumps(bill_data),
    )
    return response


def delete_bill(
    bill_id: str, book_token: str, organization_id: str
) -> requests.Response:
    response = requests.delete(
        f"https://www.zohoapis.ca/books/v3/bills/{bill_id}?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
    )

    return response


def update_bill(
    bill_id: str, bill_data: dict, book_token: str, organization_id: str
) -> requests.Response:


    response = requests.put(
        f"https://www.zohoapis.ca/books/v3/bills/{bill_id}?organization_id={organization_id}",
        headers=get_book_headers(book_token=book_token),
        data=json.dumps(bill_data),
    )

    return response
