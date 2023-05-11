from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase_ship_json_body import PurchaseShipJsonBody
from ...models.purchase_ship_response_201 import PurchaseShipResponse201
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: AuthenticatedClient,
    json_body: PurchaseShipJsonBody,
) -> Dict[str, Any]:
    url = "{}/my/ships".format(_client.base_url)

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
) -> Optional[PurchaseShipResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = PurchaseShipResponse201(**response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[PurchaseShipResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: AuthenticatedClient,
    **json_body: PurchaseShipJsonBody,
) -> Response[PurchaseShipResponse201]:
    """Purchase Ship

     Purchase a ship

    Args:
        json_body (PurchaseShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseShipResponse201]
    """

    json_body = PurchaseShipJsonBody(**json_body)

    kwargs = _get_kwargs(
        _client=_client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


def sync(
    *,
    _client: AuthenticatedClient,
    **json_body: PurchaseShipJsonBody,
) -> Optional[PurchaseShipResponse201]:
    """Purchase Ship

     Purchase a ship

    Args:
        json_body (PurchaseShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseShipResponse201
    """

    return sync_detailed(
        _client=_client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,
    **json_body: PurchaseShipJsonBody,
) -> Response[PurchaseShipResponse201]:
    """Purchase Ship

     Purchase a ship

    Args:
        json_body (PurchaseShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PurchaseShipResponse201]
    """

    json_body = PurchaseShipJsonBody(**json_body)

    kwargs = _get_kwargs(
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    *,
    _client: AuthenticatedClient,
    **json_body: PurchaseShipJsonBody,
) -> Optional[PurchaseShipResponse201]:
    """Purchase Ship

     Purchase a ship

    Args:
        json_body (PurchaseShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PurchaseShipResponse201
    """

    return (
        await asyncio_detailed(
            _client=_client,
            json_body=json_body,
        )
    ).parsed
