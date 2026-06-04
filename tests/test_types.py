from http import HTTPStatus
from io import BytesIO

from apex_dispatch_api_client.types import File, Response, UNSET


def test_unset_is_falsey() -> None:
    assert not UNSET
    assert bool(UNSET) is False


def test_file_to_tuple_matches_httpx_file_shape() -> None:
    payload = BytesIO(b"payload")
    file = File(
        payload=payload,
        file_name="tile.tif",
        mime_type="image/tiff",
    )

    assert file.to_tuple() == ("tile.tif", payload, "image/tiff")


def test_response_holds_transport_and_parsed_values() -> None:
    response = Response(
        status_code=HTTPStatus.CREATED,
        content=b'{"ok": true}',
        headers={"x-request-id": "req-123"},
        parsed={"ok": True},
    )

    assert response.status_code is HTTPStatus.CREATED
    assert response.content == b'{"ok": true}'
    assert response.headers["x-request-id"] == "req-123"
    assert response.parsed == {"ok": True}
