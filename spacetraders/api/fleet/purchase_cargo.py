from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_cargo_purchase_cargo_201_response import (
    PurchaseCargoPurchaseCargo201Response,
)
from ...models.purchase_cargo_purchase_cargo_request import (
    PurchaseCargoPurchaseCargoRequest,
)
from ...types import UNSET, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
    json_body: PurchaseCargoPurchaseCargoRequest,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/purchase".format(
        _client.base_url, shipSymbol=ship_symbol
    )

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    json_json_body = json_body.dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "follow_redirects": _client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[PurchaseCargoPurchaseCargo201Response]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = PurchaseCargoPurchaseCargo201Response(**response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PurchaseCargoPurchaseCargo201Response]:
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
    **json_body: PurchaseCargoPurchaseCargoRequest,
) -> Response[PurchaseCargoPurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoPurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseCargoPurchaseCargo201Response]
    """

    json_body = PurchaseCargoPurchaseCargoRequest(**json_body)

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        _client=_client,
        json_body=json_body,
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
    **json_body: PurchaseCargoPurchaseCargoRequest,
) -> Optional[PurchaseCargoPurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoPurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseCargoPurchaseCargo201Response
    """

    return sync_detailed(
        ship_symbol=ship_symbol,
        _client=_client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
    **json_body: PurchaseCargoPurchaseCargoRequest,
) -> Response[PurchaseCargoPurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoPurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseCargoPurchaseCargo201Response]
    """

    json_body = PurchaseCargoPurchaseCargoRequest(**json_body)

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
    **json_body: PurchaseCargoPurchaseCargoRequest,
) -> Optional[PurchaseCargoPurchaseCargo201Response]:
    """Purchase Cargo

     Purchase cargo.

    Args:
        ship_symbol (str):
        json_body (PurchaseCargoPurchaseCargoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseCargoPurchaseCargo201Response
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            _client=_client,
            json_body=json_body,
        )
    ).parsed
