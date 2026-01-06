import asyncio

import aiohttp
from rest_rpc import ApiClient

from my_api import Item, ReadItemResponse, UpdateItemResponse, api_def


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        api_client = ApiClient(
            api_def, engine="aiohttp", session=session, base_url="http://127.0.0.1:8000"
        )

        result = await api_client.read_root()
        print(result)
        assert result == {"Hello": "World"}

        result2 = await api_client.read_item(item_id=42, q="Foo")
        print(result2)
        assert result2 == ReadItemResponse(item_id=42, q="Foo")

        result3 = await api_client.update_item(
            item_id=42, item=Item(name="pie", price=3.14)
        )
        print(result3)
        assert result3 == UpdateItemResponse(item_name="pie", item_id=42)


if __name__ == "__main__":
    asyncio.run(main())
