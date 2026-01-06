import inspect
from typing import Any, Optional, Union

from pydantic import AliasChoices, AliasPath, AnyUrl
from pydantic_core import PydanticUndefined
from typing_extensions import TypedDict, deprecated


class ParamExample(TypedDict, total=False):
    summary: Optional[str]
    description: Optional[str]
    value: Optional[Any]
    externalValue: Optional[AnyUrl]
    __pydantic_config__ = {"extra": "allow"}  # type: ignore[misc]


class RequestParam:
    def __init__(self, *args, **kwargs):
        def f(
            *,
            alias: Optional[str] = None,
            alias_priority: Union[int, None] = PydanticUndefined,
            validation_alias: Union[str, AliasPath, AliasChoices, None] = None,
            serialization_alias: Union[str, None] = None,
            title: Optional[str] = None,
            description: Optional[str] = None,
            discriminator: Union[str, None] = None,
            examples: Optional[list[Any]] = None,
            openapi_examples: Optional[dict[str, ParamExample]] = None,
            deprecated: Union[deprecated, str, bool, None] = None,
            include_in_schema: bool = True,
            json_schema_extra: Union[dict[str, Any], None] = None,
        ): ...

        signature = inspect.signature(f)
        self.bound_args = signature.bind(*args, **kwargs)


class Path(RequestParam): ...


class Query(RequestParam): ...


class Body(RequestParam): ...


class Header(RequestParam): ...
