import httpx

from apex_dispatch_api_client.client import AuthenticatedClient, Client


BASE_URL = "https://dispatch.example.test"


def close_sync_clients(*clients: Client | AuthenticatedClient) -> None:
    for client in clients:
        if client._client is not None:
            client._client.close()


def test_client_creates_cached_httpx_client_with_configuration() -> None:
    timeout = httpx.Timeout(5.0)

    client = Client(
        base_url=BASE_URL,
        cookies={"session": "abc"},
        headers={"X-Client": "dispatch"},
        timeout=timeout,
        verify_ssl=False,
        follow_redirects=True,
        httpx_args={"transport": httpx.MockTransport(lambda _: httpx.Response(204))},
    )

    try:
        httpx_client = client.get_httpx_client()

        assert httpx_client is client.get_httpx_client()
        assert str(httpx_client.base_url) == BASE_URL
        assert httpx_client.headers["x-client"] == "dispatch"
        assert httpx_client.cookies["session"] == "abc"
        assert httpx_client.timeout == timeout
        assert httpx_client.follow_redirects is True
    finally:
        close_sync_clients(client)


def test_with_methods_return_evolved_client_and_update_existing_client() -> None:
    original = Client(
        base_url=BASE_URL,
        headers={"X-Original": "yes"},
        httpx_args={"transport": httpx.MockTransport(lambda _: httpx.Response(204))},
    )
    original_httpx_client = original.get_httpx_client()

    updated = (
        original.with_headers({"X-New": "yes"})
        .with_cookies({"theme": "dark"})
        .with_timeout(httpx.Timeout(7.0))
    )

    try:
        updated_httpx_client = updated.get_httpx_client()

        assert updated is not original
        assert original_httpx_client.headers["x-new"] == "yes"
        assert updated_httpx_client.headers["x-original"] == "yes"
        assert updated_httpx_client.headers["x-new"] == "yes"
        assert updated_httpx_client.cookies["theme"] == "dark"
        assert updated_httpx_client.timeout == httpx.Timeout(7.0)
    finally:
        close_sync_clients(original, updated)


def test_authenticated_client_adds_bearer_authorization_header() -> None:
    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["authorization"] = request.headers["authorization"]
        seen["trace"] = request.headers["x-trace"]
        return httpx.Response(204)

    client = AuthenticatedClient(
        base_url=BASE_URL,
        token="secret-token",
        headers={"X-Trace": "trace-1"},
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    try:
        client.get_httpx_client().get("/protected")
    finally:
        close_sync_clients(client)

    assert seen == {
        "authorization": "Bearer secret-token",
        "trace": "trace-1",
    }


def test_authenticated_client_supports_custom_raw_auth_header() -> None:
    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["api_key"] = request.headers["x-api-key"]
        return httpx.Response(204)

    client = AuthenticatedClient(
        base_url=BASE_URL,
        token="secret-token",
        prefix="",
        auth_header_name="X-Api-Key",
        httpx_args={"transport": httpx.MockTransport(handler)},
    )

    try:
        client.get_httpx_client().get("/protected")
    finally:
        close_sync_clients(client)

    assert seen["api_key"] == "secret-token"
