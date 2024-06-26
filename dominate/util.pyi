from numbers import Number
from typing import Any, Callable, Literal
from subprocess import _CMD
from dominate.dom_tag import dom_tag


def include(f: str) -> None: ...
def system(cmd: _CMD, data: bytes | None = ...) -> int: ...
def escape(s: str) -> str: ...
def unescape(s: str) -> str: ...
def url_escape(s: str) -> str: ...
def url_unescape(s: str) -> str: ...
class container(dom_tag): ...
class lazy(dom_tag):
    def __init__(
        self,
        func: Callable[..., Any],
        *args: "dom_tag" | str | Number,
        __inline: bool = ...,
        __pretty: bool = ...,
        **kwargs: str | Literal[True],
    ) -> None: ...
class text(dom_tag):
    def __init__(self, _text: str, escape: bool = ...) -> None: ...
def raw(s: str): ...
