import datetime
import unittest

import dateutil.tz

from nextDraw import nextLotteryDate


class TestNexDrawDate(unittest.TestCase):
    def testBeforeWednesday(self):
        input_date = datetime.datetime(2018, 9, 10, tzinfo=dateutil.tz.tzutc())
        self.assertEqual(nextLotteryDate(input_date),
                         datetime.datetime(2018, 9, 12, 20, 0, 0))

    def testAfterWednesday(self):
        input_date = datetime.datetime(2018, 9, 13, tzinfo=dateutil.tz.tzutc())
        self.assertEqual(nextLotteryDate(input_date),
                         datetime.datetime(2018, 9, 15, 20, 0, 0))

    def testAfterSaturdayBeforeWednesday(self):
        input_date = datetime.datetime(2018, 9, 17, tzinfo=dateutil.tz.tzutc())
        self.assertEqual(nextLotteryDate(input_date),
                         datetime.datetime(2018, 9, 19, 20, 0, 0))

    def testOnWednesdayBefore8pm(self):
        input_date = datetime.datetime(2018, 9, 12, 19, 0, 0,
                                       tzinfo=dateutil.tz.tzutc())
        self.assertEqual(nextLotteryDate(input_date),
                         datetime.datetime(2018, 9, 12, 20, 0, 0))

    def testOnWednesdayAfter8pm(self):
        input_date = datetime.datetime(2018, 9, 12, 21, 0, 0)
        self.assertEqual(nextLotteryDate(input_date),
                         datetime.datetime(2018, 9, 15, 20, 0, 0))

    def testOnSaturdayBefore8pm(self):
        input_date = datetime.datetime(2018, 9, 15, 19, 0, 0,
                                       tzinfo=dateutil.tz.tzutc())
        self.assertEqual(nextLotteryDate(input_date),
                         datetime.datetime(2018, 9, 15, 20, 0, 0))

    def testOnSaturdayAfter8pm(self):
        input_date = datetime.datetime(2018, 9, 15, 21, 0, 0,
                                       tzinfo=dateutil.tz.tzutc())
        self.assertEqual(nextLotteryDate(input_date),
                         datetime.datetime(2018, 9, 19, 20, 0, 0))

    def testForWrongDateFormat(self):
        input_date = "2018-9-15"
        self.assertEqual(nextLotteryDate(input_date),
                         "input date format is not datetime type")

    def testWithCurrentDate(self):
        self.assertGreaterEqual(nextLotteryDate(), datetime.datetime.utcnow())


if __name__ == '__main__':
    unittest.main()
