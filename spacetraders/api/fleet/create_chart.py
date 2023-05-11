from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_chart_response_201 import CreateChartResponse201
from ...types import UNSET, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/chart".format(
        _client.base_url, shipSymbol=ship_symbol
    )

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "follow_redirects": _client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[CreateChartResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateChartResponse201.update_forward_refs()
        CreateChartResponse201(**response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CreateChartResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Response[CreateChartResponse201]:
    """Create Chart

     Command a ship to chart the current waypoint.

    Waypoints in the universe are uncharted by default. These locations will not show up in the API
    until they have been charted by a ship.

    Charting a location will record your agent as the one who created the chart.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateChartResponse201]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        _client=_client,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


def sync(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Optional[CreateChartResponse201]:
    """Create Chart

     Command a ship to chart the current waypoint.

    Waypoints in the universe are uncharted by default. These locations will not show up in the API
    until they have been charted by a ship.

    Charting a location will record your agent as the one who created the chart.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateChartResponse201
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        _client=_client,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Response[CreateChartResponse201]:
    """Create Chart

     Command a ship to chart the current waypoint.

    Waypoints in the universe are uncharted by default. These locations will not show up in the API
    until they have been charted by a ship.

    Charting a location will record your agent as the one who created the chart.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateChartResponse201]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Optional[CreateChartResponse201]:
    """Create Chart

     Command a ship to chart the current waypoint.

    Waypoints in the universe are uncharted by default. These locations will not show up in the API
    until they have been charted by a ship.

    Charting a location will record your agent as the one who created the chart.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateChartResponse201
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            _client=_client,
        )
    ).parsed
