import unittest

from lruCache import LruCache


class TestLRUCache(unittest.TestCase):
    def testLru(self):
        @LruCache(maxSize=4)
        def square(x):
            return x * x

        square(2)
        square(3)
        square(4)
        square(5)
        square(6)
        self.assertIn(9, [v for v in square.cache.values()])
        self.assertIn(16, [v for v in square.cache.values()])
        self.assertIn(25, [v for v in square.cache.values()])
        self.assertIn(36, [v for v in square.cache.values()])
        self.assertNotIn(4, [v for v in square.cache.values()])
        square.clearCache()
        self.assertEqual(0, len(square.cache))

    def testLruNoMaxSize(self):
        @LruCache()
        def square(x):
            return x * x

        square(2)
        square(3)
        square(4)
        square(5)
        square(6)
        self.assertIn(9, [v for v in square.cache.values()])
        self.assertIn(16, [v for v in square.cache.values()])
        self.assertIn(25, [v for v in square.cache.values()])
        self.assertIn(36, [v for v in square.cache.values()])
        self.assertIn(4, [v for v in square.cache.values()])
        square.clearCache()
        self.assertEqual(0, len(square.cache))


if __name__ == '__main__':
    unittest.main()
