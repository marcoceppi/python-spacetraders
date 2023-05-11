from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.orbit_ship_orbit_ship_200_response import OrbitShipOrbitShip200Response
from ...types import UNSET, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/orbit".format(
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
) -> Optional[OrbitShipOrbitShip200Response]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OrbitShipOrbitShip200Response(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[OrbitShipOrbitShip200Response]:
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
) -> Response[OrbitShipOrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at it's current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrbitShipOrbitShip200Response]
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
) -> Optional[OrbitShipOrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at it's current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrbitShipOrbitShip200Response
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        _client=_client,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Response[OrbitShipOrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at it's current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrbitShipOrbitShip200Response]
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
) -> Optional[OrbitShipOrbitShip200Response]:
    """Orbit Ship

     Attempt to move your ship into orbit at it's current location. The request will only succeed if your
    ship is capable of moving into orbit at the time of the request.

    The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrbitShipOrbitShip200Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            _client=_client,
        )
    ).parsed
