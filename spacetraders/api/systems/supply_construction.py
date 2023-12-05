import json
from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.supply_construction_json_body import SupplyConstructionJsonBody
from ...models.supply_construction_response_200 import SupplyConstructionResponse200
from ...types import ApiError, Error, Response


def _get_kwargs(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
    json_body: SupplyConstructionJsonBody,
) -> Dict[str, Any]:
    url = "{}/systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply".format(
        _client.base_url, systemSymbol=system_symbol, waypointSymbol=waypoint_symbol
    )

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    json_json_body = json_body.dict(by_alias=True)

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
) -> Optional[SupplyConstructionResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SupplyConstructionResponse200(**response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[SupplyConstructionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
    raise_on_error: Optional[bool] = None,
    **json_body: SupplyConstructionJsonBody,
) -> Response[SupplyConstructionResponse200]:
    """Supply Construction Site

     Supply a construction site with the specified good. Requires a waypoint with a property of
    `isUnderConstruction` to be true.

    The good must be in your ship's cargo. The good will be removed from your ship's cargo and added to
    the construction site's materials.

    Args:
        system_symbol (str):
        waypoint_symbol (str):
        json_body (SupplyConstructionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupplyConstructionResponse200]
    """

    json_body = SupplyConstructionJsonBody.parse_obj(json_body)

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
        _client=_client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    resp = _build_response(client=_client, response=response)

    raise_on_error = (
        raise_on_error if raise_on_error is not None else _client.raise_on_error
    )
    if not raise_on_error:
        return resp

    if resp.status_code < 300:
        return resp.parsed.data

    try:
        error = json.loads(resp.content)
        details = error.get("error", {})
    except Exception:
        details = {"message": resp.content}
    raise ApiError(
        Error(
            status_code=resp.status_code,
            message=details.get("message"),
            code=details.get("code"),
            data=details.get("data"),
            headers=resp.headers,
        )
    )


async def asyncio_detailed(
    system_symbol: str,
    waypoint_symbol: str,
    *,
    _client: AuthenticatedClient,
    raise_on_error: Optional[bool] = None,
    **json_body: SupplyConstructionJsonBody,
) -> Response[SupplyConstructionResponse200]:
    """Supply Construction Site

     Supply a construction site with the specified good. Requires a waypoint with a property of
    `isUnderConstruction` to be true.

    The good must be in your ship's cargo. The good will be removed from your ship's cargo and added to
    the construction site's materials.

    Args:
        system_symbol (str):
        waypoint_symbol (str):
        json_body (SupplyConstructionJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupplyConstructionResponse200]
    """

    json_body = SupplyConstructionJsonBody.parse_obj(json_body)

    kwargs = _get_kwargs(
        system_symbol=system_symbol,
        waypoint_symbol=waypoint_symbol,
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as c:
        response = await c.request(**kwargs)

    resp = _build_response(client=_client, response=response)

    raise_on_error = (
        raise_on_error if raise_on_error is not None else _client.raise_on_error
    )
    if not raise_on_error:
        return resp

    if resp.status_code < 300:
        return resp.parsed.data

    try:
        error = json.loads(resp.content)
        details = error.get("error", {})
    except Exception:
        details = {"message": resp.content}
    raise ApiError(
        Error(
            status_code=resp.status_code,
            message=details.get("message"),
            code=details.get("code"),
            data=details.get("data"),
            headers=resp.headers,
        )
    )
