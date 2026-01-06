from typing import Annotated

import pytest
from rest_rpc import ApiClient, ApiDefinition, Query


def test_client_type_validation_error():
    api = ApiDefinition()

    @api.get("/numbers")
    def read_number(x: Annotated[int, Query()]) -> int:
        return x

    from rest_rpc import ApiImplementation

    impl = ApiImplementation(api)

    @impl.handler
    def read_number(x: int) -> int:
        return x

    app = impl.make_fastapi()
    client = ApiClient(api, "testclient", app=app)

    with pytest.raises(ValueError) as exc:
        client.read_number(x="not-an-int")

    assert 'Illegal type for parameter "x"' in str(exc.value)
