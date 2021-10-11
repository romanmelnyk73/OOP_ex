# TASK_____________________________________________________________
# You are developing a time series package
# and want to define your own class for working with dates, BetterDate.
# The attributes of the class will be year, month, and day.
# You want to have a constructor that creates BetterDate objects given the values for year, month, and day,
# but you also want to be able to create BetterDate objects from strings like 2020-04-30
# ___________________________________________________________________________

# import datetime from datetime
from datetime import datetime

class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12

    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

# Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, today):
        year = today.year
        month = today.month
        day = today.day
        return cls(year, month, day)

# Add _is_valid() checking day and month values
    def _is_valid(cls):
        if cls.day <= BetterDate._MAX_DAYS and cls.month <= BetterDate._MAX_MONTHS:
            return True
        else:
            return False

if __name__ == '__main__':

# You should be able to run the code below with no errors:
    today = datetime.today()
    bd = BetterDate.from_datetime(today)
    print(bd.year)
    print(bd.month)
    print(bd.day)

    bd1 = BetterDate(2020, 4, 30)
    print(bd1._is_valid())

    bd2 = BetterDate(2020, 6, 45)
    print(bd2._is_valid())