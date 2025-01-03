# PyZohoBooks 🚀

PyZohoBooks is a Python wrapper for interacting with Zoho Books APIs, simplifying the process of token management and making it easier to work with various endpoints for managing Zoho Books entities such as customers, vendors, bills, invoices, and items.

The library abstracts away the complexities of interacting with Zoho Books APIs by providing a simple and intuitive interface.

## Features

- **Token Management:** Automatically refresh Zoho API tokens when expired.
- **Simplified API Calls:** Easy-to-use functions to interact with customers, vendors, bills, invoices, items, and other Zoho Books resources.
- **Modular Design:** Separate modules for different aspects of Zoho Books (e.g., customers, vendors, bills, invoices).
- **Lightweight:**  Minimal dependencies for quick installation and use.

---
## Installation

Install the package directly from the repository using pip:

```bash
pip install git+https://github.com/rahul-08-11/pyzohobooks.git
```


### Setup Configuration ⚡🔑

Create a .env file in your project directory

```bash
touch .env
```

Add the following environment variables to the .env file, replacing placeholders with your actual Zoho API credentials:
```bash
ZOHO_DOMAIN_URL=https://www.zohoapis.com
ZOHO_AUTH_URL=https://accounts.zoho.com
ZOHO_REFRESH_TOKEN=your-refresh-token
ZOHO_CLIENT_ID=your-client-id
ZOHO_CLIENT_SECRET=your-client-secret
ZOHO_GRANT_TYPE=refresh_token
ZOHO_ORG_ID=your-organization-id
ZOHO_TOKEN_DIR=./
ZOHO_TOKEN_FILENAME=token.json
```

## Token Management

This package includes built-in support for managing tokens. Use the `TokenManager` utility to generate token initilizer.It handle refreshing token at regular interval to ensure the smooth functioning.

### Example

```python
from pyzohobook import TokenManager

token_instance = TokenManager()
```
Use `get_access_token()` method on token instace to fetch the token

```
token = token_instance.get_access_token()
```
The method will return a refresh token that can be use to make API calls

## Example Usage 💡

### Creating a Bill
```python
from pyzohobook import Bill

response = Bill.create_bill(
    bill_data={
        "vendor_id": "30379000000678069",
        "bill_number": "your bill number",
        "line_items": [
            {
                "item_id": "30379000000680001"
            }
        ]
    },
    book_token=token,
)

```

### Creating an Invoice

```python
from pyzohobook import Invoice

response = Invoice.create_invoice(
    invoice_data = {
        "customer_id": "3545346464364",
        "reference_number": "your reference number",
        "line_items": [
            {
                "item_id": "30379000000680001"
            }
        ]},
    book_token=token

)

```

### Mark an Invoice

```python
from pyzohobook import Invoice

response = Invoice.mark_invoice(
    invoice_id="your invoice id",
    book_token=token,
    status="sent"
)
``` 

### Search an Item

```python
from pyzohobook import Item

response = Item.search_item(
    item_name="MyItemName", 
    book_token=token

)
```

### Fetch an Invoice as a PDF

```python
from pyzohobook import Invoice

response = Invoice.fetch_invoice(
    invoice_id="your invoice id",
    book_token=token,
    formate="pdf"
)
```

## Contributing 🤝

While PyZohoBooks currently covers some key API functionalities, there are still many other Zoho Books API wrappers and endpoints that can be added to improve the library. Contributions are extremely welcome! If you encounter any issues, have new feature ideas, or want to implement additional API wrappers, please feel free to:

1. Fork the repository
2. Create a branch
3. Implement the feature or fix the issue
4. Submit a pull request with your changes

Your contributions can help make this library even more powerful and flexible for everyone using Zoho Books to Automate there Business Using Python.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
