from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from typing import Any
from collections.abc import Awaitable, Callable
from contextvars import ContextVar, copy_context


class Globals:
    __slots__ = ("_vars", "_defaults")

    _vars: dict[str, ContextVar]
    _defaults: dict[str, Any]

    def __init__(self) -> None:
        object.__setattr__(self, '_vars', {})
        object.__setattr__(self, '_defaults', {})

    def set_default(self, name: str, default: Any) -> None:
        if (
            name in self._defaults
            and default in self._defaults[name]
        ):
            return
        if name in self._vars:
            raise RuntimeError(
                f"Cannot set default as variable {name} was already set",
            )
        self._defaults[name] = default

    def _get_default_value(self, name: str) -> Any:
        default = self._defaults.get(name, None)
        return default() if callable(default) else default

    def _ensure_var(self, name: str) -> None:
        if name not in self._vars:
            default = self._get_default_value(name)
            self._vars[name] = ContextVar(f"globals:{name}", default=default)

    def __getattr__(self, name: str) -> Any:
        self._ensure_var(name)
        return self._vars[name].get()

    def __setattr__(self, name: str, value: Any) -> None:
        self._ensure_var(name)
        self._vars[name].set(value)


async def global_middleware_dispatch(
        request: Request, call_next: Callable
) -> Response:
    ctx = copy_context()

    def _call_next() -> Awaitable[Response]:
        return call_next(request)

    return await ctx.run(_call_next)


class MyBaseHTTPMiddleware(BaseHTTPMiddleware):

    async def __call__(self, scope, receive, send):
        try:
            await super().__call__(scope, receive, send)
        except RuntimeError as exc:
            if str(exc) == 'No response returned.':
                request = Request(scope, receive=receive)
                if await request.is_disconnected():
                    return
            raise

    async def dispatch(self, request, call_next):
        raise NotImplementedError()


class GlobalMiddleware(MyBaseHTTPMiddleware):
    def __init__(self, app: ASGIApp) -> None:
        super().__init__(app, global_middleware_dispatch)


g = Globals()
