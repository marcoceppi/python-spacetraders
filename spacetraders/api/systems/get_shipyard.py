from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_shipyard_response_200 import GetShipyardResponse200
from ...types import UNSET, Response


def _get_kwargs(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard".format(
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
) -> Optional[GetShipyardResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetShipyardResponse200.update_forward_refs()
        GetShipyardResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GetShipyardResponse200]:
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
) -> Response[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipyardResponse200]
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
) -> Optional[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShipyardResponse200
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
) -> Response[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetShipyardResponse200]
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
) -> Optional[GetShipyardResponse200]:
    """Get Shipyard

     Get the shipyard for a waypoint.

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetShipyardResponse200
    """

    return (
        await asyncio_detailed(
            system_symbol=system_symbol,
            waypoint_symbol=waypoint_symbol,
            _client=_client,
        )
    ).parsed
