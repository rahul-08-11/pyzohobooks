from datetime import datetime, timedelta
import requests
import os
import json



class TokenManager:
    _token = None
    _expiry = None

    def __init__(self, domain_name) ->  None:
        self.domain_url =  self._get_domain_url(domain_name.lower())
        self.refresh_token = None
        self.client_id = None
        self.client_secret = None
        self.grant_type = ""

    def _get_domain_url(self,domain_name) -> str:
        zoho_urls = {
            "united states": "https://accounts.zoho.com/",
            "europe": "https://accounts.zoho.eu/",
            "india": "https://accounts.zoho.in/",
            "australia": "https://accounts.zoho.com.au/",
            "japan": "https://accounts.zoho.jp/",
            "canada": "https://accounts.zohocloud.ca/"
        }
        return zoho_urls[domain_name]

    def _get_access_token(self) -> str:
        # store at project level
        if os.path.exists("token.json"):
            pass

        else:
            with open("token.json","w") as f:
                self._refresh_token()
                f.write(json.dumps({"token": self._token, "expiry": self._expiry.strftime("%Y-%m-%d %H:%M:%S")}))

        if self._token is None or self._is_token_expired():
            self._refresh_token()
        return self._token

    def _is_token_expired(self) -> bool:
        # Assuming the token is valid for 50 minutes
        return self._expiry is None or datetime.now() >= self._expiry

    def _refresh_token(self) -> None:
        # Call the Zoho API to refresh the token
        url = f"{self.domain_url}oauth/v2/token"
        print(url)
        ## prepare the parameters
        params = {
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": self.grant_type,
        }
        ## send post request
        response = requests.post(url, params=params)
        print(response.json())
        if response.status_code == 200:
            self._expiry = datetime.now() + timedelta(minutes=50)  # Update expiry time
            print("expirey time is set", self._expiry)
            self._token = response.json()["access_token"]


TokenManager("Canada")._get_access_token()