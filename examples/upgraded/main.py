from rest_rpc import ApiImplementation

from my_api import ReadItemResponse, UpdateItemResponse, api_def

api_impl = ApiImplementation(api_def)


@api_impl.handler
def read_root():
    return {"Hello": "World"}


@api_impl.handler
def read_item(item_id, q):
    return ReadItemResponse(item_id=item_id, q=q)


@api_impl.handler
def update_item(item_id, item):
    return UpdateItemResponse(item_name=item.name, item_id=item_id)


app = api_impl.make_fastapi()
