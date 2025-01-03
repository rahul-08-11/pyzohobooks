# pyzohobook/token_manager.py

import json
import requests
from datetime import datetime, timedelta
import os
from . import config


class TokenManager:
    """
    A class for managing Zoho Books API tokens.

    Attributes:
        _token (str): The current access token.
        _expiry (datetime): The expiration time of the current access token.

    Methods:
        _refresh_token(): Refreshes the access token by calling the Zoho API.

        _is_token_expired(): Checks if the current access token is expired.

        get_access_token(): Retrieves the current access token.

        _get_domain_url(): Retrieves the domain URL based on the domain name.

    Instance Variables:
        domain_url (str): The base URL for the Zoho Books API.
        refresh_token (str): The refresh token for the Zoho Books API.
        client_id (str): The client ID for the Zoho Books API.
        client_secret (str): The client secret for the Zoho Books API.
        grant_type (str): The grant type for the Zoho Books API.

    """

    _token = None
    _expiry = None

    def __init__(self) -> None:
        self.config = config.Config()
        self._load_token_from_file()

    def _load_token_from_file(self) -> None:
        """Loads the token and expiry from the token file if it exists."""
        if os.path.exists(self.config.token_path):
            try:
                with open(self.config.token_path, "r") as f:
                    data = json.load(f)
                    self._token = data.get("token")
                    expiry_str = data.get("expiry")
                    if expiry_str:
                        self._expiry = datetime.strptime(
                            expiry_str, "%Y-%m-%d %H:%M:%S"
                        )
            except (json.JSONDecodeError, FileNotFoundError, KeyError):
                # If the file is corrupted or missing data, reset token and expiry
                self._token = None
                self._expiry = None

    def _save_token_to_file(self) -> None:
        """Saves the current token and expiry to the token file."""
        with open(self.config.token_path, "w") as f:
            json.dump(
                {
                    "token": self._token,
                    "expiry": self._expiry.strftime("%Y-%m-%d %H:%M:%S"),
                },
                f,
            )

    def get_access_token(self) -> str:
        """Retrieves the current access token, refreshing it if necessary."""
        if self._token is None or self._is_token_expired():
            self._refresh_token()
        return self._token

    def _is_token_expired(self) -> bool:
        """Checks if the current access token is expired."""
        return self._expiry is None or datetime.now() >= self._expiry

    def _refresh_token(self) -> None:
        """Calls the Zoho API to refresh the token."""
        url = f"{self.config.auth_url}/oauth/v2/token"

        print(url)
        params = {
            "refresh_token": self.config.refresh_token,
            "client_id": self.config.client_id,
            "client_secret": self.config.client_secret,
            "grant_type": self.config.grant_type,
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            self._token = response.json()["access_token"]
            self._expiry = datetime.now() + timedelta(minutes=50)  # Update expiry time
            self._save_token_to_file()  # Save the new token and expiry to file
        else:
            raise Exception(
                f"Failed to refresh token: {response.status_code}, {response.text}"
            )
