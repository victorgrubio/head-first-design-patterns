"""Singleton Implementation"""
from typing import Any


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some possible methods
    include: base class, decorator, metaclass. We will use the meta class
    """

    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            instance: Singleton = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Singleton implementation using the previously defined metaclass. This will allow us to separate the pattern implementation
    from the bussiness logic of the element
    """
    pass