"""
Implement a least recently used (LRU) cache mechanism using a decorator
and demonstrate it use in a small script. The LRU must be able to admit
 a max_size parameter that by default has to be 100.
"""
from _thread import RLock
from collections import OrderedDict


class LruCache(object):
    """ LRU cache implemention as decorator """

    def __init__(self, maxSize=100):
        self.cache = OrderedDict()
        self.maxSize = maxSize
        self.lock = RLock()  # because updates aren't threadsafe

    def clearCache(self):
        with self.lock:
            self.cache.clear()

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            kwtuple = tuple((key, kwargs[key])
                            for key in sorted(kwargs.keys()))
            key = (args, kwtuple)

            # Here I am using 3 different locks for update, insert and delete

            # Check if key already exits then delete the item and
            # add it back at the end of dictionary(make it most recently used)
            if key in self.cache:
                with self.lock:
                    value = self.cache[key]
                    del self.cache[key]
                    self.cache[key] = value
                    return value

            # when cache is full, pop item from front of dictionary
            # as this is least recently used
            if len(self.cache) == self.maxSize:
                with self.lock:
                    self.cache.popitem(last=False)

            # if key does not exist in the system then insert it at the end
            #  of dictionary(most recent used items will go in the end)
            with self.lock:
                value = func(*args, **kwargs)
                self.cache[key] = value
                return value

        wrapper.cache = self.cache
        wrapper.maxSize = self.maxSize
        wrapper.clearCache = self.clearCache
        return wrapper
