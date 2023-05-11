from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_my_agent_response_200 import GetMyAgentResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/my/agent".format(_client.base_url)

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
) -> Optional[GetMyAgentResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetMyAgentResponse200.update_forward_refs()
        GetMyAgentResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[GetMyAgentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: AuthenticatedClient,
) -> Response[GetMyAgentResponse200]:
    """My Agent Details

     Fetch your agent's details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyAgentResponse200]
    """

    kwargs = _get_kwargs(
        _client=_client,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


def sync(
    *,
    _client: AuthenticatedClient,
) -> Optional[GetMyAgentResponse200]:
    """My Agent Details

     Fetch your agent's details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMyAgentResponse200
    """

    return sync_detailed(
        _client=_client,
    ).parsed


async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,
) -> Response[GetMyAgentResponse200]:
    """My Agent Details

     Fetch your agent's details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMyAgentResponse200]
    """

    kwargs = _get_kwargs(
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    *,
    _client: AuthenticatedClient,
) -> Optional[GetMyAgentResponse200]:
    """My Agent Details

     Fetch your agent's details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMyAgentResponse200
    """

    return (
        await asyncio_detailed(
            _client=_client,
        )
    ).parsed
