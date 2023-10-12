import json
from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extract_resources_with_survey_response_201 import (
    ExtractResourcesWithSurveyResponse201,
)
from ...models.survey import Survey
from ...types import ApiError, Error, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
    json_body: Survey,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/extract/survey".format(
        _client.base_url, shipSymbol=ship_symbol
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
) -> Optional[ExtractResourcesWithSurveyResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ExtractResourcesWithSurveyResponse201(**response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[ExtractResourcesWithSurveyResponse201]:
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
    raise_on_error: Optional[bool] = None,
    **json_body: Survey,
) -> Response[ExtractResourcesWithSurveyResponse201]:
    """Extract Resources with Survey

     Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the
    payload, which allows your ship to extract specific yields.

    Send the full survey object as the payload which will be validated according to the signature. If
    the signature is invalid, or any properties of the survey are changed, the request will fail.

    Args:
        ship_symbol (str):
        json_body (Survey): A resource survey of a waypoint, detailing a specific extraction
            location and the types of resources that can be found there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResourcesWithSurveyResponse201]
    """

    json_body = Survey.parse_obj(json_body)

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
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
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
    raise_on_error: Optional[bool] = None,
    **json_body: Survey,
) -> Response[ExtractResourcesWithSurveyResponse201]:
    """Extract Resources with Survey

     Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the
    payload, which allows your ship to extract specific yields.

    Send the full survey object as the payload which will be validated according to the signature. If
    the signature is invalid, or any properties of the survey are changed, the request will fail.

    Args:
        ship_symbol (str):
        json_body (Survey): A resource survey of a waypoint, detailing a specific extraction
            location and the types of resources that can be found there.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtractResourcesWithSurveyResponse201]
    """

    json_body = Survey.parse_obj(json_body)

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
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
