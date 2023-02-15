#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from functools import wraps
from typing import Any, Callable, Optional, Union
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """Count the no. of times a method is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores history of inputs and outputs for a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input = method.__qualname__ + ':inputs'
        output = method.__qualname__ + ':outputs'
        self._redis.rpush(input, str(args))
        values = method(self, *args, **kwargs)
        self._redis.rpush(output, values)
        return values
    return wrapper


class Cache:

    """Writes strings to Redis"""

    def __init__(self) -> None:
        """store a Redis instance as private variable and flush it"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[bytes, str, int, float]) -> str:
        """generates a random key, stores data using it and returns it"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """uses the callable to convert the data to original type"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Convert to string"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """convert to int"""
        data = self._redis.get(key)
        try:
            data = int(data.decode('utf-8'))
        except Exception:
            data = 0
        return data
