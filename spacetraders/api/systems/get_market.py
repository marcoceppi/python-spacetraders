from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_market_response_200 import GetMarketResponse200
from ...types import UNSET, Response


def _get_kwargs(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/systems/{systemSymbol}/waypoints/{waypointSymbol}/market".format(
        _client.base_url, systemSymbol=system_symbol, waypointSymbol=waypoint_symbol
    )

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "follow_redirects": _client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[GetMarketResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetMarketResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GetMarketResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Response[GetMarketResponse200]:
    """Get Market

     Retrieve imports, exports and exchange data from a marketplace. Imports can be sold, exports can be
    purchased, and exchange goods can be purchased or sold. Send a ship to the waypoint to access trade
    good prices and recent transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketResponse200]
    """

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
        _client=_client,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


def sync(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Optional[GetMarketResponse200]:
    """Get Market

     Retrieve imports, exports and exchange data from a marketplace. Imports can be sold, exports can be
    purchased, and exchange goods can be purchased or sold. Send a ship to the waypoint to access trade
    good prices and recent transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketResponse200
    """

    return sync_detailed(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
        _client=_client,
    ).parsed


async def asyncio_detailed(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Response[GetMarketResponse200]:
    """Get Market

     Retrieve imports, exports and exchange data from a marketplace. Imports can be sold, exports can be
    purchased, and exchange goods can be purchased or sold. Send a ship to the waypoint to access trade
    good prices and recent transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMarketResponse200]
    """

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Optional[GetMarketResponse200]:
    """Get Market

     Retrieve imports, exports and exchange data from a marketplace. Imports can be sold, exports can be
    purchased, and exchange goods can be purchased or sold. Send a ship to the waypoint to access trade
    good prices and recent transactions.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMarketResponse200
    """

    return (
        await asyncio_detailed(
            system_symbol=system_symbol,
            waypoint_symbol=waypoint_symbol,
            _client=_client,
        )
    ).parsed
