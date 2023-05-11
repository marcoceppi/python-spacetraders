from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_waypoints_response_200 import GetSystemWaypointsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    system_symbol: str,
    *,
    _client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/systems/{systemSymbol}/waypoints".format(
        _client.base_url, systemSymbol=system_symbol
    )

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "follow_redirects": _client.follow_redirects,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[GetSystemWaypointsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSystemWaypointsResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GetSystemWaypointsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_symbol: str,
    *,
    _client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[GetSystemWaypointsResponse200]:
    """List Waypoints

     Fetch all of the waypoints for a given system. System must be charted or a ship must be present to
    return waypoint details.

    Args:
        system_symbol (str):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemWaypointsResponse200]
    """

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        _client=_client,
        page=page,
        limit=limit,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


def sync(
    system_symbol: str,
    *,
    _client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[GetSystemWaypointsResponse200]:
    """List Waypoints

     Fetch all of the waypoints for a given system. System must be charted or a ship must be present to
    return waypoint details.

    Args:
        system_symbol (str):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemWaypointsResponse200
    """

    return sync_detailed(
        system_symbol=system_symbol,
        _client=_client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    system_symbol: str,
    *,
    _client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Response[GetSystemWaypointsResponse200]:
    """List Waypoints

     Fetch all of the waypoints for a given system. System must be charted or a ship must be present to
    return waypoint details.

    Args:
        system_symbol (str):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSystemWaypointsResponse200]
    """

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        _client=_client,
        page=page,
        limit=limit,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    system_symbol: str,
    *,
    _client: AuthenticatedClient,
    page: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
) -> Optional[GetSystemWaypointsResponse200]:
    """List Waypoints

     Fetch all of the waypoints for a given system. System must be charted or a ship must be present to
    return waypoint details.

    Args:
        system_symbol (str):
        page (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSystemWaypointsResponse200
    """

    return (
        await asyncio_detailed(
            system_symbol=system_symbol,
            _client=_client,
            page=page,
            limit=limit,
        )
    ).parsed
