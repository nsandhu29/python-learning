import sys
from abc import ABC, abstractmethod

# def print_table(objects, colnames):
#     """
#     Make a nicely formatted table showing attributes from a list of objects
#     """
#     for colname in colnames:
#         print('{:>10s}'.format(colname), end=' ')
#     print()
#     for obj in objects:
#         for colname in colnames:
#             print('{:>10s}'.format(str(getattr(obj, colname))), end =' ')
#         print()

class TableFormatter(ABC):

    def __init__(self, outfile=None):
        if outfile == None:
            outfile = sys.stdout
        self.outfile = outfile

    # Serves as design spec for making tables
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError

def print_table(objects, colnames, formatter):
    """
    Make a nicely formatted table showing attributes from a list of objects
    """
    if not isinstance(formatter, TableFormatter):
        raise TypeError('formatter must be a tableformatter')

    formatter.headings(colnames)
    for obj in objects:
        rowdata = [str(getattr(obj,colname)) for colname in colnames]
        formatter.row(rowdata)


class TextTableFormatter(TableFormatter):
    def __init__(self, outfile=None, width =10):
        super().__init__(outfile)
        self.width

    def headings(self, headers):
        for header in headers:
            print('{:>{}s}'.format(header, self.width), end=' ', file = self.outfile)
        print()

    def row(self, rowdata):
        for item in rowdata:
            print('{:>{}s}'.format(item, self.width), end=' ', file = self.outfile)
        print()


class QuotedTextTableFormatter(TextTableFormatter):
    def row(self, rowdata):
        #Put Quotes around all values
        quoted = ['"{}"'.format(d) for d in rowdata]
        super().row(quoted)


class QuotedMixin(object):
    def row(self, rowdata):
        quoted = ['"{}"'.format(d) for d in rowdata]
        super.row(quoted)


class Formatter(QuotedMixin, TextTableFormatter):
    pass

