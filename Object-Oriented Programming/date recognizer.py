'''
I made a year, date, day recognizer.
The EvenBetterDate finds the format by just giving it the string
This gives two options, and the easier one is EvenBetterDate
'''
#!Though all the classes have the same method name "from_str", they do different things depending on the class.
# *Users don't need to remember many method names this way.

class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
        # Recall that Python allows multiple variable assignments in one line
        self.year, self.month, self.day = year, month, day

    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and  convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)


class EvenBetterDate(BetterDate):
    @classmethod
    def from_str(cls, datestr, format):
        if format == "YYYY-MM-DD":
            return BetterDate.from_str(datestr)
        elif format == "MM-DD-YYYY":
            month, day, year = map(int, datestr.split("-"))
            return cls(year, month, day)


class BestDate(EvenBetterDate):
    @classmethod
    def from_str(cls, datestr):
        first, second, third = datestr.split("-")
        if len(first) == 4 and len(second) == 2 and len(third) == 2:
            return EvenBetterDate.from_str(datestr, "YYYY-MM-DD")
        elif len(first) == 2 and len(second) == 2 and len(third) == 4:
            return EvenBetterDate.from_str(datastr, "MM-DD-YYYY")


bd = BetterDate.from_str('2020-04-30')
print(bd.year)
print(bd.month)
print(bd.day)


a = EvenBetterDate.from_str("2004-08-07", "YYYY-MM-DD")
print(a.year)
b = EvenBetterDate.from_str("07-08-2004", "MM-DD-YYYY")
print(b.year)

c = BestDate.from_str("2000-01-01")
print(c.year)
