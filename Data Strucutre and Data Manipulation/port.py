import csv
import json


def read_portfolio(filename, *, errors='warn'):
    '''
    Read a csv file with name, date, share and price data into list
    :param *:
    :param filename:
    :return:
    '''
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Erros must be one of 'warn', 'silent', 'raise'")
    portfolio = []  # list of records
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip headers row
        # row_no = 0
        for rowno, row in enumerate(rows, start=1):
            # row_no += 1
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row', row)
                    print('Row:', rowno, 'Reason:', err)
                continue  # Skips to next row
            # record = tuple(row)
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
            }
            portfolio.append(record)

    return portfolio


portfolio = read_portfolio('portfolio.csv', errors='silent')
print(portfolio)
total = 0.0
# for holding in portfolio:
#     total += holding[2] * holding[3]  # Shares * price

# for name, date, shares, price in portfolio:
#     total += shares * price

for holding in portfolio:
    total += holding['shares'] * holding['price']


# Sorting data
def holding_name(holding):
    return holding['name']


portfolio.sort(key=holding_name)
for holding in portfolio:
    print(holding)

sort_portfolio2 = portfolio.sort(key=lambda holding: holding['name'])
min_price = min(portfolio, key=lambda holding: holding['price'])
max_share = max(portfolio, key= lambda holding: holding['shares'])


# group the data
import itertools
for name, items in itertools.groupby(portfolio, key=lambda holding: holding['name']):
    print('Name:', name)
    for it in items:
        print('   ', it)

by_name = {name: list(items)
           for name, items in itertools.groupby(portfolio, key=lambda holding: holding['name'])}
