#pyzohobook/config.py
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    """
    A singleton class for managing application configuration.

    The `Config` class ensures that there is only one instance of the configuration throughout the application.
    It provides attributes for various configuration values such as domain URL, authentication details, and file paths.

    Attributes:
        domain_url (str): The base URL of the API domain.
        auth_url (str): The URL for authentication requests.
        refresh_token (str): The refresh token for OAuth2 authentication.
        client_id (str): The client ID for OAuth2 authentication.
        client_secret (str): The client secret for OAuth2 authentication.
        grant_type (str): The grant type for OAuth2 authentication (e.g., "refresh_token").
        organization_id (str): The ID of the organization (if applicable).
        token_dir (str): The directory where the token file is stored.
        token_filename (str): The name of the token file.
        token_path (str): The full path to the token file (constructed automatically).
    """

    _instance = None  # Class-level variable to store the singleton instance

    def __new__(cls, *args, **kwargs):
        """
        Overrides the `__new__` method to ensure only one instance of the class is created.

        Returns:
            Config: The singleton instance of the Config class.
        """
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Initializes the Config instance with environment variable values.

        Uses the following environment variables:
            - ZOHO_DOMAIN_URL
            - ZOHO_AUTH_URL
            - ZOHO_REFRESH_TOKEN
            - ZOHO_CLIENT_ID
            - ZOHO_CLIENT_SECRET
            - ZOHO_GRANT_TYPE
            - ZOHO_ORG_ID
            - ZOHO_TOKEN_DIR
            - ZOHO_TOKEN_FILENAME
        """
        if not hasattr(self, "initialized"):  # Ensure initialization only happens once
            self.domain_url = os.getenv("ZOHO_DOMAIN_URL", "https://www.zohoapis.com")
            self.auth_url = os.getenv("ZOHO_AUTH_URL", "https://accounts.zoho.com")
            self.refresh_token = os.getenv("ZOHO_REFRESH_TOKEN")
            self.client_id = os.getenv("ZOHO_CLIENT_ID")
            self.client_secret = os.getenv("ZOHO_CLIENT_SECRET")
            self.grant_type = os.getenv("ZOHO_GRANT_TYPE")
            self.organization_id = os.getenv("ZOHO_ORG_ID")
            self.token_dir = os.getenv("ZOHO_TOKEN_DIR", "./")
            self.token_filename = os.getenv("ZOHO_TOKEN_FILENAME", "token.json")
            self.initialized = True  # Mark as initialized
            self.token_path = os.path.join(self.token_dir, self.token_filename)

    def __getattr__(self, name):
        """
        Handles dynamic attribute access.

        Args:
            name (str): The name of the attribute to access.

        Returns:
            Any: The value of the requested attribute.

        Raises:
            AttributeError: If the attribute does not exist in the instance.
        """
        if name in self.__dict__:
            return getattr(self, name)
        else:
            raise AttributeError(
                f"'{self.__class__.__name__}' object has no attribute '{name}'"
            )

    def __setattr__(self, name, value):
        """
        Prevents accidental modification of configuration values after they are set.

        Args:
            name (str): The name of the attribute to set.
            value (Any): The value of the attribute to set.

        Raises:
            AttributeError: If an attempt is made to modify an existing attribute.
        """
        if name not in self.__dict__:  # Allow setting new attributes only
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Cannot modify the attribute '{name}' once it's set.")
