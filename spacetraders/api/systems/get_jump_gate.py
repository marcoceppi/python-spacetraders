import json
from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_jump_gate_response_200 import GetJumpGateResponse200
from ...types import ApiError, Error, Response


def _get_kwargs(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate".format(
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
) -> Optional[GetJumpGateResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetJumpGateResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GetJumpGateResponse200]:
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
    raise_on_error: Optional[bool] = None,
) -> Response[GetJumpGateResponse200]:
    """Get Jump Gate

     Get jump gate details for a waypoint. Requires a waypoint of type `JUMP_GATE` to use.

    Waypoints connected to this jump gate can be

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJumpGateResponse200]
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
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
    raise_on_error: Optional[bool] = None,
) -> Response[GetJumpGateResponse200]:
    """Get Jump Gate

     Get jump gate details for a waypoint. Requires a waypoint of type `JUMP_GATE` to use.

    Waypoints connected to this jump gate can be

    Args:
        system_symbol (str):
        waypoint_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetJumpGateResponse200]
    """

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
        _client=_client,
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
