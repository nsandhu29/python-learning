import csv


class Holding(object):

    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, newprice):
        if not isinstance(newprice, float):
            raise TypeError('Expected float')
        if newprice < 0:
            raise ValueError('Must >= 0')
        self._price = newprice

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, newshares):
        if not isinstance(newshares, int):
            raise TypeError('Expected int')
        self._shares = newshares


    def __repr__(self):
        return 'holding({!r},{!r},{!r},{!r})'.format(self.name, self.shares, self.date, self.price)

    def __str__(self):
        return '{} shares of {} at {:0.2f}'.format(self.shares, self.name, self.price)

    @property
    def cost(self):
        return self.shares * self._price

    def sell(self, nshares):
        self.shares -= nshares


class Portfolio():
    def __init__(self):
        self.holdings = []

    def __getattr__(self, item):
        return getattr(self.holdings, item)


    # def append(self, item):
    #     self.holdings.append(item)
    #
    # def insert(self, index, item):
    #     self.holdings.insert(index, item)


    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                h = Holding(row[0], row[1], int(row[2]), float(row[3]))
                self.holdings.append(h)
        return self

    def total_cost(self):
        return sum[([h.shares * h.price for h in self.holdings])]

    # def size(self):
    #     return len(self.holdings)
    #
    # def getHolding(self):
    #     return self.holdings[n]

    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, item):
        if isinstance(item, str):
            return [h for h in self.holdings if h.name == item]
        return self.holdings[item]

    def __iter__(self):
        return self.holdings.__iter__()

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            h = Holding(row[0], row[1], int(row[2]), float(row[3]))
            portfolio.append(h)
    return portfolio