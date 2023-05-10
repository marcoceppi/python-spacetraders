from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dock_ship_dock_ship_200_response import DockShipDockShip200Response
from ...types import UNSET, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/dock".format(
        client.base_url, shipSymbol=ship_symbol
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[DockShipDockShip200Response]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DockShipDockShip200Response.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[DockShipDockShip200Response]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[DockShipDockShip200Response]:
    """Dock Ship

     Attempt to dock your ship at it's current location. Docking will only succeed if the waypoint is a
    dockable location, and your ship is capable of docking at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DockShipDockShip200Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DockShipDockShip200Response]:
    """Dock Ship

     Attempt to dock your ship at it's current location. Docking will only succeed if the waypoint is a
    dockable location, and your ship is capable of docking at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DockShipDockShip200Response
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[DockShipDockShip200Response]:
    """Dock Ship

     Attempt to dock your ship at it's current location. Docking will only succeed if the waypoint is a
    dockable location, and your ship is capable of docking at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DockShipDockShip200Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DockShipDockShip200Response]:
    """Dock Ship

     Attempt to dock your ship at it's current location. Docking will only succeed if the waypoint is a
    dockable location, and your ship is capable of docking at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DockShipDockShip200Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
        )
    ).parsed
