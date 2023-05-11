from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.navigate_ship_json_body import NavigateShipJsonBody
from ...models.navigate_ship_response_200 import NavigateShipResponse200
from ...types import UNSET, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
    json_body: NavigateShipJsonBody,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/navigate".format(
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
) -> Optional[NavigateShipResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NavigateShipResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[NavigateShipResponse200]:
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
    **json_body: NavigateShipJsonBody,
) -> Response[NavigateShipResponse200]:
    """Navigate Ship

     Navigate to a target destination. The destination must be located within the same system as the
    ship. Navigating will consume the necessary fuel and supplies from the ship's manifest, and will pay
    out crew wages from the agent's account.

    The returned response will detail the route information including the expected time of arrival. Most
    ship actions are unavailable until the ship has arrived at it's destination.

    To travel between systems, see the ship's warp or jump actions.

    Args:
        ship_symbol (str):
        json_body (NavigateShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NavigateShipResponse200]
    """

    json_body = NavigateShipJsonBody(**json_body)

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
    **json_body: NavigateShipJsonBody,
) -> Optional[NavigateShipResponse200]:
    """Navigate Ship

     Navigate to a target destination. The destination must be located within the same system as the
    ship. Navigating will consume the necessary fuel and supplies from the ship's manifest, and will pay
    out crew wages from the agent's account.

    The returned response will detail the route information including the expected time of arrival. Most
    ship actions are unavailable until the ship has arrived at it's destination.

    To travel between systems, see the ship's warp or jump actions.

    Args:
        ship_symbol (str):
        json_body (NavigateShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NavigateShipResponse200
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
    **json_body: NavigateShipJsonBody,
) -> Response[NavigateShipResponse200]:
    """Navigate Ship

     Navigate to a target destination. The destination must be located within the same system as the
    ship. Navigating will consume the necessary fuel and supplies from the ship's manifest, and will pay
    out crew wages from the agent's account.

    The returned response will detail the route information including the expected time of arrival. Most
    ship actions are unavailable until the ship has arrived at it's destination.

    To travel between systems, see the ship's warp or jump actions.

    Args:
        ship_symbol (str):
        json_body (NavigateShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NavigateShipResponse200]
    """

    json_body = NavigateShipJsonBody(**json_body)

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
    **json_body: NavigateShipJsonBody,
) -> Optional[NavigateShipResponse200]:
    """Navigate Ship

     Navigate to a target destination. The destination must be located within the same system as the
    ship. Navigating will consume the necessary fuel and supplies from the ship's manifest, and will pay
    out crew wages from the agent's account.

    The returned response will detail the route information including the expected time of arrival. Most
    ship actions are unavailable until the ship has arrived at it's destination.

    To travel between systems, see the ship's warp or jump actions.

    Args:
        ship_symbol (str):
        json_body (NavigateShipJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NavigateShipResponse200
    """

    return (
        await asyncio_detailed(
            ship_symbol=ship_symbol,
            _client=_client,
            json_body=json_body,
        )
    ).parsed
