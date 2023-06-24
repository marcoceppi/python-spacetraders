import json
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_system_waypoints_response_200 import GetSystemWaypointsResponse200
from ...types import UNSET, ApiError, Error, Response, Unset


def _get_kwargs(
    system_symbol: str,
    *,
    _client: AuthenticatedClient,
    page: Union[Unset, None, int] = 1,
    limit: Union[Unset, None, int] = 10,
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
    raise_on_error: Optional[bool] = None,
    page: Union[Unset, None, int] = 1,
    limit: Union[Unset, None, int] = 10,
) -> Response[GetSystemWaypointsResponse200]:
    """List Waypoints in System

     Return a paginated list of all of the waypoints for a given system.

    If a waypoint is uncharted, it will return the `Uncharted` trait instead of its actual traits.

    Args:
        system_symbol (str):
        page (Union[Unset, None, int]):  Default: 1.
        limit (Union[Unset, None, int]):  Default: 10.

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

    resp = _build_response(client=_client, response=response)

    raise_on_error = (
        raise_on_error if raise_on_error is not None else _client.raise_on_error
    )
    if not raise_on_error:
        return resp

    if resp.status_code < 300:
        return resp.parsed.data

    try:
        error = json.loads(resp.content)
        details = error.get("error", {})
    except Exception:
        details = {"message": resp.content}
    raise ApiError(
        Error(
            status_code=resp.status_code,
            message=details.get("message"),
            code=details.get("code"),
            data=details.get("data"),
            headers=resp.headers,
        )
    )


async def asyncio_detailed(
    system_symbol: str,
    *,
    _client: AuthenticatedClient,
    raise_on_error: Optional[bool] = None,
    page: Union[Unset, None, int] = 1,
    limit: Union[Unset, None, int] = 10,
) -> Response[GetSystemWaypointsResponse200]:
    """List Waypoints in System

     Return a paginated list of all of the waypoints for a given system.

    If a waypoint is uncharted, it will return the `Uncharted` trait instead of its actual traits.

    Args:
        system_symbol (str):
        page (Union[Unset, None, int]):  Default: 1.
        limit (Union[Unset, None, int]):  Default: 10.

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

    resp = _build_response(client=_client, response=response)

    raise_on_error = (
        raise_on_error if raise_on_error is not None else _client.raise_on_error
    )
    if not raise_on_error:
        return resp

    if resp.status_code < 300:
        return resp.parsed.data

    try:
        error = json.loads(resp.content)
        details = error.get("error", {})
    except Exception:
        details = {"message": resp.content}
    raise ApiError(
        Error(
            status_code=resp.status_code,
            message=details.get("message"),
            code=details.get("code"),
            data=details.get("data"),
            headers=resp.headers,
        )
    )
