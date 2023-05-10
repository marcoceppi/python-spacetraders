from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sell_cargo_sell_cargo_201_response import SellCargoSellCargo201Response
from ...models.sell_cargo_sell_cargo_request import SellCargoSellCargoRequest
from ...types import UNSET, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    json_body: SellCargoSellCargoRequest,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/sell".format(
        client.base_url, shipSymbol=ship_symbol
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[SellCargoSellCargo201Response]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SellCargoSellCargo201Response.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[SellCargoSellCargo201Response]:
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
    json_body: SellCargoSellCargoRequest,
) -> Response[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellCargoSellCargo201Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        client=client,
        json_body=json_body,
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
    json_body: SellCargoSellCargoRequest,
) -> Optional[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellCargoSellCargo201Response
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    json_body: SellCargoSellCargoRequest,
) -> Response[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SellCargoSellCargo201Response]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ship_symbol: str,
    *,
    client: AuthenticatedClient,
    json_body: SellCargoSellCargoRequest,
) -> Optional[SellCargoSellCargo201Response]:
    """Sell Cargo

     Sell cargo.

    Args:
        ship_symbol (str):
        json_body (SellCargoSellCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SellCargoSellCargo201Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            client=client,
            json_body=json_body,
        )
    ).parsed
