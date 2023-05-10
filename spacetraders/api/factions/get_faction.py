from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_faction_response_200 import GetFactionResponse200
from ...types import UNSET, Response


def _get_kwargs(
    faction_symbol: str = "CGR",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/factions/{factionSymbol}".format(
        client.base_url, factionSymbol=faction_symbol
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
) -> Optional[GetFactionResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFactionResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GetFactionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    faction_symbol: str = "CGR",
    *,
    client: Client,
) -> Response[GetFactionResponse200]:
    """Get Faction

     View the details of a faction.

    Args:
        faction_symbol (str):  Default: 'CGR'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFactionResponse200]
    """

    kwargs = _get_kwargs(
        faction_symbol=faction_symbol,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    faction_symbol: str = "CGR",
    *,
    client: Client,
) -> Optional[GetFactionResponse200]:
    """Get Faction

     View the details of a faction.

    Args:
        faction_symbol (str):  Default: 'CGR'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFactionResponse200
    """

    return sync_detailed(
        faction_symbol=faction_symbol,
        client=client,
    ).parsed


async def asyncio_detailed(
    faction_symbol: str = "CGR",
    *,
    client: Client,
) -> Response[GetFactionResponse200]:
    """Get Faction

     View the details of a faction.

    Args:
        faction_symbol (str):  Default: 'CGR'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFactionResponse200]
    """

    kwargs = _get_kwargs(
        faction_symbol=faction_symbol,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    faction_symbol: str = "CGR",
    *,
    client: Client,
) -> Optional[GetFactionResponse200]:
    """Get Faction

     View the details of a faction.

    Args:
        faction_symbol (str):  Default: 'CGR'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFactionResponse200
    """

    return (
        await asyncio_detailed(
            faction_symbol=faction_symbol,
            client=client,
        )
    ).parsed
