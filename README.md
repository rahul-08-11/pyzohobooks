# PyZohoBooks

PyZohoBooks is a Python library designed to simplify interactions with Zoho Books APIs. It provides a streamlined way to handle token refresh operations and offers easy-to-use functions for making API calls, avoiding the complexities and lengthiness of Zoho's official API documentation.

## Features

- **Token Management:** Automatically refresh Zoho API tokens when expired.
- **Simplified API Calls:** Easy-to-use functions for common operations such as handling customers, vendors, bills, invoices, and items.
- **Modular Design:** Organized modules for different aspects of Zoho Books (e.g., customers, vendors, bills).
- **Lightweight:** Minimal dependencies for ease of installation and usage.

---
## Installation

Install the package directly from the repository using pip:

```bash
pip install git+https://github.com/rahul-08-11/pyzohobooks.git
```


### Example Operations

#### Create a Record
```python
response = api.create_record(moduleName="Leads", data={"Company": "Acme Corp", "Last_Name": "Doe"}, token="your_access_token")
print(response.json())
```

#### Read Records
```python
response = api.read_record(moduleName="Leads", token="your_access_token")
print(response.json())
```

#### Update a Record
```python
response = api.update_record(moduleName="Leads", id="record_id", data={"Last_Name": "Smith"}, token="your_access_token")
print(response.json())
```

#### Partially Update a Record
```python
response = api.patch_record(moduleName="Leads", id="record_id", data={"First_Name": "John"}, token="your_access_token")
print(response.json())
```

#### Delete a Record
```python
response = api.delete_record(moduleName="Leads", id="record_id", token="your_access_token")
print(response.json())
```

#### Attach a File
```python
response = api.attach_file(moduleName="Leads", record_id="record_id", file_path="/path/to/file.pdf", token="your_access_token")
print(response.json())
```

#### Fetch All Attachments
```python
response = api.fetch_file(moduleName="Leads", record_id="record_id", token="your_access_token")
print(response.json())
```

#### Fetch a Specific File Attachment
```python
response = api.fetch_file(moduleName="Leads", record_id="record_id", file_id="file_id", token="your_access_token", fetch_all=False)
with open("downloaded_file.pdf", "wb") as file:
    file.write(response.content)
```


## Token Management

This package includes built-in support for managing tokens. Use the `TokenManager` utility to generate token initilizer.

### Example

```python
from pyzohocrm import TokenManager

token_instance = TokenManager(domain_name="Canada",
                                            refresh_token="####.######.##################",
                                            client_id="########.#######################",
                                            client_secret="####################.#######################",
                                            grant_type="refresh_token")
```
Use `get_access_token()` method on token instace to fetch the token

```
token = token_instance.get_access_token()
```

## Logging

ZOHOAPI uses Python's built-in `logging` module to log errors and API events. Customize logging levels as needed for your application.

```python
import logging
logging.basicConfig(level=logging.INFO)
```

## Contributing

Feel free to contribute by submitting issues or pull requests in the Git repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
