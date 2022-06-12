# pcost.py
#
# Exercise 1.27, 2.15

import csv
import sys


def portfolio_cost(filename: str) -> float:
    with open(filename, 'rt') as f:
        total = 0
        rows = csv.reader(f)
        headers = next(f).replace("\n", "").split(',')
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

        return total


def main(argv):
    port_total = portfolio_cost(argv[1])
    print(f'Total cost: {port_total}')


if __name__ == '__main__':
    main(sys.argv)
