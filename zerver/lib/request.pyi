# This mypy stubs file ensures that mypy can correctly analyze REQ.
from typing import Any, Callable, Text, TypeVar
from django.http import HttpResponse

ViewFuncT = TypeVar('ViewFuncT', bound=Callable[..., HttpResponse])

class JsonableError(Exception):
    msg = ...  # type: Text
    status_code = ...  # type: int
    def __init__(self, msg: Text) -> None: ...
    def to_json_error_msg(self) -> Text: ...

class RequestVariableMissingError(JsonableError): ...
class RequestVariableConversionError(JsonableError): ...

def REQ(*args: Any, **kwargs: Any) -> Any: ...

def has_request_variables(view_func: ViewFuncT) -> ViewFuncT: ...
