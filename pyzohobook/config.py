import os

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

    def __init__(
        self,
        domain_url: str = None,
        auth_url: str = None,
        refresh_token: str = None,
        client_id: str = None,
        client_secret: str = None,
        grant_type: str = None,
        organization_id: str = None,
        token_dir: str = "./",
        token_filename: str = "token.json",
    ) -> None:
        """
        Initializes the Config instance with provided or default configuration values.

        Args:
            domain_url (str, optional): The base URL of the API domain. Defaults to None.
            auth_url (str, optional): The URL for authentication requests. Defaults to None.
            refresh_token (str, optional): The refresh token for OAuth2 authentication. Defaults to None.
            client_id (str, optional): The client ID for OAuth2 authentication. Defaults to None.
            client_secret (str, optional): The client secret for OAuth2 authentication. Defaults to None.
            grant_type (str, optional): The grant type for OAuth2 authentication. Defaults to None.
            organization_id (str, optional): The ID of the organization. Defaults to None.
            token_dir (str, optional): The directory where the token file is stored. Defaults to "./".
            token_filename (str, optional): The name of the token file. Defaults to "token.json".
        """
        if not hasattr(self, "initialized"):  # Ensure initialization only happens once
            self.domain_url = domain_url
            self.auth_url = auth_url
            self.refresh_token = refresh_token
            self.client_id = client_id
            self.client_secret = client_secret
            self.grant_type = grant_type
            self.organization_id = organization_id
            self.token_dir = token_dir
            self.token_filename = token_filename
            self.token_path = os.path.join(token_dir, token_filename)
            self.initialized = True  # Marks the instance as initialized

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
