#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from typing import Any, Callable, Optional, Union
from uuid import uuid4


class Cache:

    """Writes strings to Redis"""

    def __init__(self) -> None:
        """store a Redis instance as private variable and flush it"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, str, int, float]) -> str:
        """generates a random key, stores data using it and returns it"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[Any], Any]) -> Any:
        """uses the callable to convert the data to original type"""
        data = self._redis.get(key)
        if data:
            return fn(data)

    def get_str(self, data: bytes) -> str:
        """Convert to string"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """convert to int"""
        return int.from_bytes(data, 'big')
