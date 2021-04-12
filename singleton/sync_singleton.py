"""Synchronized Singleton in Python. Thread-safe implementation"""
from typing import Any
from threading import Lock, Thread


class SingletonMeta(type):
    """
    Thread-safe implementation of Singleton pattern
    """

    _instances = {}
    _lock: Lock = Lock()

    """
    We now have a lock object that will be used to synchronize threads during
    first access to Singleton
    """

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """
        Possible changes to the value of the __init__ argument do not affect the returned instance
        """
        # Now, imagine that the program has just been launched. Since there's no Singleton instance yet,
        # multiple threads can simultaneously pass the previous conditional and reach this point almost
        # at the same time. The first of them will acquire lock and will proceed further while the rest
        # will wait here.
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional, goes inside and creates
            # the Singleton instance. Once it leaves the lock block,  a thread that might have been
            # waiting for the lock release may enter this section. But since the singleton field
            # is already initialized, the thread won't create a new object
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SyncSingleton(metaclass=SingletonMeta):
    value: str = ""
    """
    We will use this property to prove that our Singleton implementation works
    """

    def __init__(self, value: str):
        self.value = value