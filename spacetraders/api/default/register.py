from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.register_json_body import RegisterJsonBody
from ...models.register_response_201 import RegisterResponse201
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: Client,
    json_body: RegisterJsonBody,
) -> Dict[str, Any]:
    url = "{}/register".format(_client.base_url)

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
) -> Optional[RegisterResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = RegisterResponse201(**response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[RegisterResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    **json_body: RegisterJsonBody,
) -> Response[RegisterResponse201]:
    """Register New Agent

     Creates a new agent and ties it to a temporary Account.

    The agent symbol is a 3-14 character string that will represent your agent. This symbol will prefix
    the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.

    A new agent will be granted an authorization token, a contract with their starting faction, a
    command ship with a jump drive, and one hundred thousand credits.

    > #### Keep your token safe and secure
    >
    > Save your token during the alpha phase. There is no way to regenerate this token without starting
    a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders
    website.

    You can accept your contract using the `/my/contracts/{contractId}/accept` endpoint. You will want
    to navigate your command ship to a nearby asteroid field and execute the
    `/my/ships/{shipSymbol}/extract` endpoint to mine various types of ores and minerals.

    Return to the contract destination and execute the `/my/ships/{shipSymbol}/deliver` endpoint to
    deposit goods into the contract.

    When your contract is fulfilled, you can call `/my/contracts/{contractId}/fulfill` to retrieve
    payment.

    Args:
        json_body (RegisterJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterResponse201]
    """

    json_body = RegisterJsonBody(**json_body)

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
    _client: Client,
    **json_body: RegisterJsonBody,
) -> Optional[RegisterResponse201]:
    """Register New Agent

     Creates a new agent and ties it to a temporary Account.

    The agent symbol is a 3-14 character string that will represent your agent. This symbol will prefix
    the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.

    A new agent will be granted an authorization token, a contract with their starting faction, a
    command ship with a jump drive, and one hundred thousand credits.

    > #### Keep your token safe and secure
    >
    > Save your token during the alpha phase. There is no way to regenerate this token without starting
    a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders
    website.

    You can accept your contract using the `/my/contracts/{contractId}/accept` endpoint. You will want
    to navigate your command ship to a nearby asteroid field and execute the
    `/my/ships/{shipSymbol}/extract` endpoint to mine various types of ores and minerals.

    Return to the contract destination and execute the `/my/ships/{shipSymbol}/deliver` endpoint to
    deposit goods into the contract.

    When your contract is fulfilled, you can call `/my/contracts/{contractId}/fulfill` to retrieve
    payment.

    Args:
        json_body (RegisterJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterResponse201
    """

    return sync_detailed(
        _client=_client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    **json_body: RegisterJsonBody,
) -> Response[RegisterResponse201]:
    """Register New Agent

     Creates a new agent and ties it to a temporary Account.

    The agent symbol is a 3-14 character string that will represent your agent. This symbol will prefix
    the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.

    A new agent will be granted an authorization token, a contract with their starting faction, a
    command ship with a jump drive, and one hundred thousand credits.

    > #### Keep your token safe and secure
    >
    > Save your token during the alpha phase. There is no way to regenerate this token without starting
    a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders
    website.

    You can accept your contract using the `/my/contracts/{contractId}/accept` endpoint. You will want
    to navigate your command ship to a nearby asteroid field and execute the
    `/my/ships/{shipSymbol}/extract` endpoint to mine various types of ores and minerals.

    Return to the contract destination and execute the `/my/ships/{shipSymbol}/deliver` endpoint to
    deposit goods into the contract.

    When your contract is fulfilled, you can call `/my/contracts/{contractId}/fulfill` to retrieve
    payment.

    Args:
        json_body (RegisterJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterResponse201]
    """

    json_body = RegisterJsonBody(**json_body)

    kwargs = _get_kwargs(
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    *,
    _client: Client,
    **json_body: RegisterJsonBody,
) -> Optional[RegisterResponse201]:
    """Register New Agent

     Creates a new agent and ties it to a temporary Account.

    The agent symbol is a 3-14 character string that will represent your agent. This symbol will prefix
    the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.

    A new agent will be granted an authorization token, a contract with their starting faction, a
    command ship with a jump drive, and one hundred thousand credits.

    > #### Keep your token safe and secure
    >
    > Save your token during the alpha phase. There is no way to regenerate this token without starting
    a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders
    website.

    You can accept your contract using the `/my/contracts/{contractId}/accept` endpoint. You will want
    to navigate your command ship to a nearby asteroid field and execute the
    `/my/ships/{shipSymbol}/extract` endpoint to mine various types of ores and minerals.

    Return to the contract destination and execute the `/my/ships/{shipSymbol}/deliver` endpoint to
    deposit goods into the contract.

    When your contract is fulfilled, you can call `/my/contracts/{contractId}/fulfill` to retrieve
    payment.

    Args:
        json_body (RegisterJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterResponse201
    """

    return (
        await asyncio_detailed(
            _client=_client,
            json_body=json_body,
        )
    ).parsed
