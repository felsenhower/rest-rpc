from typing import Annotated

from typed_rest import ApiClient, ApiClientEngine, ApiDefinition, Header


def test_single_header_roundtrip():
    api = ApiDefinition()

    @api.get("/ping")
    def ping(h: Annotated[str, Header()]) -> str:
        return h

    from typed_rest import ApiImplementation

    impl = ApiImplementation(api)

    @impl.handler
    def ping(h: str) -> str:
        return h

    app = impl.make_fastapi()
    client = ApiClient(api, ApiClientEngine.TESTCLIENT, app=app)

    assert client.ping(h="hello") == "hello"
