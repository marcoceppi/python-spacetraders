import ssl
from functools import partial
from importlib import import_module
from typing import Dict, Union

import attr


class APIStub:
    """A module importer that traverses the api directory based on getattr"""

    def __init__(self, client, mod, exec_mode):
        self._module = mod
        self._client = client
        self._exec_mode = exec_mode

    def __getattr__(self, attr):
        if not hasattr(self._module, attr):
            imp = import_module(f".{attr}", self._module.__package__)
        else:
            imp = getattr(self._module, attr)

        if not hasattr(imp, self._exec_mode):
            return APIStub(client=self._client, mod=imp, exec=self._exec_mode)

        return partial(getattr(imp, self._exec_mode), _client=self._client)


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API

    Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document.
        follow_redirects: Whether or not to follow redirects. Default value is False.
    """

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)
    raise_on_unexpected_status: bool = attr.ib(False, kw_only=True)
    follow_redirects: bool = attr.ib(False, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)

    def _build_api_stub(self, path, exec_mode):
        myimp = import_module(f".api.{path}", "spacetraders")
        return APIStub(client=self, mod=myimp, exec_mode=exec_mode)

    def __getattr__(self, attr):
        return self._build_api_stub(attr, "sync_detailed")


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    token: str
    prefix: str = "Bearer"
    auth_header_name: str = "Authorization"

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"{self.prefix} {self.token}" if self.prefix else self.token
        return {self.auth_header_name: auth_header_value, **self.headers}


class AsyncClient(Client):
    """An async Client for unsecured endpoints"""

    def __getattr__(self, attr):
        return self._build_api_stub(attr, "asyncio_detailed")


class AuthenticatedAsyncClient(AuthenticatedClient):
    """An async Client which has been authenticated for use on secured endpoints"""

    def __getattr__(self, attr):
        return self._build_api_stub(attr, "asyncio_detailed")
