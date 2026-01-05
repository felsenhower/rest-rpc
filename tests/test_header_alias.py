from typing import Annotated

from typed_rest import ApiClient, ApiClientEngine, ApiDefinition, Header


def test_header_alias():
    api = ApiDefinition()

    @api.get("/alias")
    def alias_header(token: Annotated[str, Header(alias="X-Auth-Token")]) -> str:
        return token

    from typed_rest import ApiImplementation

    impl = ApiImplementation(api)

    @impl.handler
    def alias_header(token: str) -> str:
        return token

    app = impl.make_fastapi()
    client = ApiClient(api, ApiClientEngine.TESTCLIENT, app=app)

    assert client.alias_header(token="abc") == "abc"
