import unittest

from anargam import getAnagrams, isAnagram


class TestAnagrams(unittest.TestCase):
    def testPositiveWithTuple(self):
        self.assertEqual(getAnagrams('dam', ('dam', 'ma d', 'mam')),
                         ['dam', 'ma d'])

    def testPositiveWithList(self):
        inputList = ['pastier', 'pirates', 'traipse', 'piratis']
        expectedOutput = ['pastier', 'pirates', 'traipse']
        self.assertEqual(getAnagrams('parties', inputList), expectedOutput)

    def testPositiveWithSpace(self):
        inputList = ['Ogdred Weary', 'Regera Dowdy', 'E G Deadworry']
        expectedOutput = ['Ogdred Weary', 'Regera Dowdy', 'E G Deadworry']
        self.assertEqual(getAnagrams('Edward Gorey', inputList),
                         expectedOutput)

    def testNegative(self):
        self.assertNotEqual(getAnagrams('abc', ['abc', 'cba', 'ba']), ['ba'])

    def testIsAnagramPositive(self):
        self.assertEqual(isAnagram('mad', 'dam'), True)

    def testIsAnagramNegative(self):
        self.assertEqual(isAnagram('mad', 'dams'), False)

    def testException(self):
        self.assertRaises(TypeError, getAnagrams(1, [1, 2, 3]), [1])


if __name__ == '__main__':
    unittest.main()
