from . import reader   #Package - relative import


def read_portfolio(filename, *, errors='warn'):
    return reader.read_csv(filename, [str, str, int, float], errors=errors)




if __name__ == '__main__':
    portfolio = read_portfolio('../portfolio.csv')
    total = 0.0
    for holding in portfolio:
        total += holding['shares']*holding['price']

    print(total)