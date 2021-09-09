# Setting up processing pipelines
# unix command tail -f filename
# setup pipes
# tail -f filename | egrep "IBM|MSFT|CAT|AA"

import csv


def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

for line in follow('stocklog.csv'):
    row = line.split(',')
    change = float(row[4])
    if change < 0:
        name = row[0]
        price = row[1]
        print('{:>10s}, {:>10s}, {:10.2f}'.format(name, price, change))


rows = csv.reader(lines)
rows.__next__()


def grep(names, row):
    for row in rows:
        if row[0] in names:
            yield row

matching = grep(['MSFT', 'AAP', 'IBM'], rows)
matching.__next__()



types = [str, float, str, str, float, float, float, float, float, int]
converted = ( [func(val) for func, val in zip(types, row)] for row in matching)
converted
negchange = (row for row in converted if row[4] < 0)


def parse_stock(lines):
    rows = csv.reader(lines)
    types = [str, float, str, str, float, float, float, float, float, int]
    converted = ([func(val) for func, val in zip(types, row)] for row in matching)
    return converted

lines = follow('filename')
rows = parse_stock(lines)
negchange = (row for row in converted if row[4] < 0)
