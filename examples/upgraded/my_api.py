from typing import Annotated

from pydantic import BaseModel
from rest_rpc import ApiDefinition, Body, Query

api_def = ApiDefinition()


class ReadItemResponse(BaseModel):
    item_id: int
    q: str | None


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class UpdateItemResponse(BaseModel):
    item_name: str
    item_id: int


@api_def.get("/")
def read_root() -> dict[str, str]: ...


@api_def.get("/items/{item_id}")
def read_item(
    item_id: int, q: Annotated[str | None, Query()] = None
) -> ReadItemResponse: ...


@api_def.put("/items/{item_id}")
def update_item(item_id: int, item: Annotated[Item, Body()]) -> UpdateItemResponse: ...
