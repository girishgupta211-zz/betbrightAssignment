import unittest

from lruCache import LruCache


class TestLRUCache(unittest.TestCase):
    def testLru(self):
        @LruCache(maxSize=2)
        def square(x):
            return x * x

        square(2)
        square(3)
        square(4)
        self.assertIn(9, [v for v in square.cache.values()])
        self.assertIn(16, [v for v in square.cache.values()])
        self.assertNotIn(4, [v for v in square.cache.values()])
        square.clearCache()
        self.assertEqual(0, len(square.cache))


if __name__ == '__main__':
    unittest.main()
