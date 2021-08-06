import csv

def read_csv(filename, types, *, errors='warn'):
    ''':type
    Read csv file with type converstion into list of dicts
    '''
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Errors must be 'warn', 'silent', 'raise'")

    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad Row', row)
                    print('Row', rowno, 'Reason', err)
                elif errors == 'raise':
                    raise
                else:
                    pass
                continue
            record = dict(zip(header, row))
            records.append(record)
    return records