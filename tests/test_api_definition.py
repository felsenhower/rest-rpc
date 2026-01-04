from typing import Annotated

import pytest
from pydantic import BaseModel
from typed_rest import ApiDefinition, Body, Query


def test_add_simple_routes():
    api_def = ApiDefinition()

    @api_def.get("/")
    def simple_route() -> dict[str, str]: ...

    @api_def.get("/items/{item_id}")
    def route_with_arg(item_id: int) -> dict[str, str]: ...

    @api_def.get("/items/{item_id}")
    def route_with_optional_arg(
        item_id: int, q: Annotated[str | None, Query()] = None
    ) -> dict[str, str]: ...


class ExampleResult(BaseModel):
    item_id: int
    q: str | None


def test_add_basemodel_route():
    api_def = ApiDefinition()

    @api_def.get("/items/{item_id}")
    def route_with_optional_arg(
        item_id: int, q: Annotated[str | None, Query()] = None
    ) -> ExampleResult: ...


class Item(BaseModel):
    name: str
    price: float


def test_post():
    api_def = ApiDefinition()

    @api_def.post("/items/{item_id}")
    def update_item(item_id: int, item: Annotated[Item, Body()]) -> ExampleResult: ...


def test_detect_missing_return_annotation():
    api_def = ApiDefinition()
    with pytest.raises(ValueError):

        @api_def.get("/")
        def simple_route(): ...


def test_detect_missing_type_annotation():
    api_def = ApiDefinition()
    with pytest.raises(ValueError):

        @api_def.get("/")
        def route_with_arg(item_id: int, q) -> dict[str, str]: ...


def test_detect_kwargs():
    api_def = ApiDefinition()
    with pytest.raises(ValueError):

        @api_def.get("/")
        def kwargs_route(**kwargs) -> dict[str, str]: ...


def test_detect_args():
    api_def = ApiDefinition()
    with pytest.raises(ValueError):

        @api_def.get("/")
        def args_route(*args) -> dict[str, str]: ...


def test_detect_invalid_parameter_annotation():
    api_def = ApiDefinition()
    with pytest.raises(ValueError):

        @api_def.get("/")
        def route_with_arg(x: any) -> dict[str, str]: ...


def test_detect_invalid_return_annotation():
    api_def = ApiDefinition()
    with pytest.raises(ValueError):

        @api_def.get("/")
        def simple_route(**kwargs) -> dict[str, any]: ...
