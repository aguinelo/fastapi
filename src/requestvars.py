import contextvars
import types
import typing

user = contextvars.ContextVar("user", default=types.SimpleNamespace())


# This is the only public API
def request_user():
    return user.get()
