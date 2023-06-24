import json
from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_survey_response_201 import CreateSurveyResponse201
from ...types import ApiError, Error, Response


def _get_kwargs(
    ship_symbol: str,
    *,
    _client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/my/ships/{shipSymbol}/survey".format(
        _client.base_url, shipSymbol=ship_symbol
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
) -> Optional[CreateSurveyResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateSurveyResponse201(**response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[CreateSurveyResponse201]:
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
) -> Response[CreateSurveyResponse201]:
    """Create Survey

     Create surveys on a waypoint that can be extracted such as asteroid fields. A survey focuses on
    specific types of deposits from the extracted location. When ships extract using this survey, they
    are guaranteed to procure a high amount of one of the goods in the survey.

    In order to use a survey, send the entire survey details in the body of the extract request.

    Each survey may have multiple deposits, and if a symbol shows up more than once, that indicates a
    higher chance of extracting that resource.

    Your ship will enter a cooldown after surveying in which it is unable to perform certain actions.
    Surveys will eventually expire after a period of time or will be exhausted after being extracted
    several times based on the survey's size. Multiple ships can use the same survey for extraction.

    A ship must have the `Surveyor` mount installed in order to use this function.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSurveyResponse201]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        _client=_client,
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
) -> Response[CreateSurveyResponse201]:
    """Create Survey

     Create surveys on a waypoint that can be extracted such as asteroid fields. A survey focuses on
    specific types of deposits from the extracted location. When ships extract using this survey, they
    are guaranteed to procure a high amount of one of the goods in the survey.

    In order to use a survey, send the entire survey details in the body of the extract request.

    Each survey may have multiple deposits, and if a symbol shows up more than once, that indicates a
    higher chance of extracting that resource.

    Your ship will enter a cooldown after surveying in which it is unable to perform certain actions.
    Surveys will eventually expire after a period of time or will be exhausted after being extracted
    several times based on the survey's size. Multiple ships can use the same survey for extraction.

    A ship must have the `Surveyor` mount installed in order to use this function.

    Args:
        ship_symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSurveyResponse201]
    """

    kwargs = _get_kwargs(
        ship_symbol=ship_symbol,
        _client=_client,
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
