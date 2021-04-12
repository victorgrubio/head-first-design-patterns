from sync_singleton import SyncSingleton
from threading import Thread
import unittest


def create_singleton(value: str) -> str:
    """Return singleton value

    Args:
        value (str): Value to include in string
    """
    singleton: SyncSingleton = SyncSingleton(value)
    return singleton.value

class TestSyncSingleton(unittest.TestCase):

    def test_sync_singletion(self):
        process1 = Thread(target=create_singleton, args=("FOO",))
        process2 = Thread(target=create_singleton, args=("BAR",))
        process1.start()
        process2.start()