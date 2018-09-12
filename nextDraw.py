import datetime


# Calculating next valid draw date
# The Irish lottery draw takes place twice weekly
# on a Wednesday and a Saturday at 8pm. Write a
# function that calculates and returns the next
# valid draw date based on an optional supplied date
# time parameter. If no supplied date is provided, assume current date time

def nextLotteryDate(inputDate=None):
    """ Calculate and return the next valid Irish Lotto draw date.
           input_date = datetime object (optional, default value is current
           date/time)
    """

    # 0 = Monday, 1 = Tuesday, 2 = Wednesday, .... 6 = Sunday

    wednesday = 2
    saturday = 5
    if inputDate is None:
        inputDate = datetime.datetime.utcnow()
    else:
        if not isinstance(inputDate, datetime.datetime):
            return "input date format is not datetime type"

    # after 19:59 you've missed draw, so get the next date
    if inputDate.hour >= 20:
        inputDate += datetime.timedelta(days=1)

    # Get week day from input date
    dayOfWeek = inputDate.weekday()

    if dayOfWeek in (wednesday, saturday):
        days = 0

    elif dayOfWeek < wednesday:
        days = wednesday - dayOfWeek

    elif dayOfWeek < saturday:
        days = saturday - dayOfWeek

    # case to handle sunday
    else:
        days = 3

    return datetime.datetime.combine(
        (inputDate + datetime.timedelta(days=days)).date(),
        datetime.time(20, 00))
