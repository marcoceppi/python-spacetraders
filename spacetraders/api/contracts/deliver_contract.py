from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deliver_contract_json_body import DeliverContractJsonBody
from ...models.deliver_contract_response_200 import DeliverContractResponse200
from ...types import UNSET, Response


def _get_kwargs(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
    json_body: DeliverContractJsonBody,
) -> Dict[str, Any]:
    url = "{}/my/contracts/{contractId}/deliver".format(
        _client.base_url, contractId=contract_id
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
) -> Optional[DeliverContractResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeliverContractResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[DeliverContractResponse200]:
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
    **json_body: DeliverContractJsonBody,
) -> Response[DeliverContractResponse200]:
    """Deliver Contract

     Deliver cargo on a given contract.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverContractResponse200]
    """

    json_body = DeliverContractJsonBody(**json_body)

    kwargs = _get_kwargs(
        contract_id=contract_id,
        _client=_client,
        json_body=json_body,
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
    **json_body: DeliverContractJsonBody,
) -> Optional[DeliverContractResponse200]:
    """Deliver Contract

     Deliver cargo on a given contract.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverContractResponse200
    """

    return sync_detailed(
        contract_id=contract_id,
        _client=_client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
    **json_body: DeliverContractJsonBody,
) -> Response[DeliverContractResponse200]:
    """Deliver Contract

     Deliver cargo on a given contract.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliverContractResponse200]
    """

    json_body = DeliverContractJsonBody(**json_body)

    kwargs = _get_kwargs(
        contract_id=contract_id,
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    return _build_response(client=_client, response=response)


async def asyncio(
    contract_id: str,
    *,
    _client: AuthenticatedClient,
    **json_body: DeliverContractJsonBody,
) -> Optional[DeliverContractResponse200]:
    """Deliver Contract

     Deliver cargo on a given contract.

    Args:
        contract_id (str):
        json_body (DeliverContractJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliverContractResponse200
    """

    return (
        await asyncio_detailed(
            contract_id=contract_id,
            _client=_client,
            json_body=json_body,
        )
    ).parsed
