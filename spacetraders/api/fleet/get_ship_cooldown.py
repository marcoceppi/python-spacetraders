from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ship_cooldown_response_200 import GetShipCooldownResponse200
from ...types import UNSET, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/cooldown".format(
        client.base_url, shipSymbol=ship_symbol
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, GetShipCooldownResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetShipCooldownResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, GetShipCooldownResponse200]]:
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
) -> Response[Union[Any, GetShipCooldownResponse200]]:
    """Get Ship Cooldown

     Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump
    drive, scanning, or extracting resources taxes your reactor and results in a cooldown.

    Your ship cannot perform additional actions until your cooldown has expired. The duration of your
    cooldown is relative to the power consumption of the related modules or mounts for the action taken.

    Response returns a 204 status code (no-content) when the ship has no cooldown.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetShipCooldownResponse200]]
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
) -> Optional[Union[Any, GetShipCooldownResponse200]]:
    """Get Ship Cooldown

     Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump
    drive, scanning, or extracting resources taxes your reactor and results in a cooldown.

    Your ship cannot perform additional actions until your cooldown has expired. The duration of your
    cooldown is relative to the power consumption of the related modules or mounts for the action taken.

    Response returns a 204 status code (no-content) when the ship has no cooldown.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetShipCooldownResponse200]
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetShipCooldownResponse200]]:
    """Get Ship Cooldown

     Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump
    drive, scanning, or extracting resources taxes your reactor and results in a cooldown.

    Your ship cannot perform additional actions until your cooldown has expired. The duration of your
    cooldown is relative to the power consumption of the related modules or mounts for the action taken.

    Response returns a 204 status code (no-content) when the ship has no cooldown.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetShipCooldownResponse200]]
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
) -> Optional[Union[Any, GetShipCooldownResponse200]]:
    """Get Ship Cooldown

     Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump
    drive, scanning, or extracting resources taxes your reactor and results in a cooldown.

    Your ship cannot perform additional actions until your cooldown has expired. The duration of your
    cooldown is relative to the power consumption of the related modules or mounts for the action taken.

    Response returns a 204 status code (no-content) when the ship has no cooldown.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetShipCooldownResponse200]
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
        )
    ).parsed
