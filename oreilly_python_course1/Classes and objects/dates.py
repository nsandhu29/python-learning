# demonstrate multiple init methods
import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, s):  # cls is 'Date'
        parts = s.split('-')
        return cls(int(parts[0]), int(parts[1]), int(parts[2]))

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)




# def date_from_string(s):
#     parts = s.split('-')
#     return Date(int(parts[0]), int(parts[1]), int(parts[2]))

