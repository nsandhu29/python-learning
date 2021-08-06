import csv


def portfolio_cost(filename, *, errors='warn'):
    '''
    Compute total shares*price for a csv file with name, date, share and price data
    :param *:
    :param filename:
    :return:
    '''
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Erros must be one of 'warn', 'silent', 'raise'")

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
            total += row[2] * row[3]
    return total


total = portfolio_cost('../Data Strucutre and Data Manipulation/portfolio.csv', errors='warn')
print('Total Cost', total)
