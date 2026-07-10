import time
from functools import wraps
from typing import Any, Callable


def retry(max_tries: int = 3, delay: float = 2.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any: return func(*args, **kwargs)
        return wrapper
    return decorator
