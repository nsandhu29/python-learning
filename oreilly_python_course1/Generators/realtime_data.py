# watch log file on server tail -f Data/stock.csv
# Watch a log file in stocks

import os


f = open('filename', 'r')
f.seek(0, os.SEEK_END)

while True:
    line = f.readline()
    if not line:
        time.sleep(0.1)
        continue # retry
    row = line.split(',')
    change = float(row[4])
    if change < 0:
        name = row[0]

    print('Got:', line)



# Packaging iteration in function
def follow('filename'):
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