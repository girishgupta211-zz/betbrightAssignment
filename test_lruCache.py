import unittest

from lruCache import LruCache


class TestLRUCache(unittest.TestCase):
    def testLru(self):
        @LruCache(maxSize=4)
        def square(x):
            return x * x

        for num in range(2, 7):
            square(num)

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

        for num in range(105):
            square(num)
        self.assertNotIn(16, [v for v in square.cache.values()])
        self.assertNotIn(0, [v for v in square.cache.values()])
        self.assertNotIn(9, [v for v in square.cache.values()])
        self.assertNotIn(((4,), ()), [v for v in square.cache.keys()])
        self.assertIn(((5,), ()), [v for v in square.cache.keys()])
        self.assertIn(((104,), ()), [v for v in square.cache.keys()])
        square.clearCache()
        self.assertEqual(0, len(square.cache))


if __name__ == '__main__':
    unittest.main()
