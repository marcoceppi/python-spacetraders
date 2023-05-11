from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fulfill_contract_response_200 import FulfillContractResponse200
from ...types import UNSET, Response


def _get_kwargs(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/my/contracts/{contractId}/fulfill".format(
        _client.base_url, contractId=contract_id
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
) -> Optional[FulfillContractResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FulfillContractResponse200.update_forward_refs()
        FulfillContractResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[FulfillContractResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
) -> Response[FulfillContractResponse200]:
    """Fulfill Contract

     Fulfill a contract

    Args:
        contract_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FulfillContractResponse200]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
        _client=_client,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


def sync(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
) -> Optional[FulfillContractResponse200]:
    """Fulfill Contract

     Fulfill a contract

    Args:
        contract_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FulfillContractResponse200
    """

    return sync_detailed(
        contract_id=contract_id,
        _client=_client,
    ).parsed


async def asyncio_detailed(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
) -> Response[FulfillContractResponse200]:
    """Fulfill Contract

     Fulfill a contract

    Args:
        contract_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FulfillContractResponse200]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
) -> Optional[FulfillContractResponse200]:
    """Fulfill Contract

     Fulfill a contract

    Args:
        contract_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FulfillContractResponse200
    """

    return (
        await asyncio_detailed(
            contract_id=contract_id,
            _client=_client,
        )
    ).parsed
