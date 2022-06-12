# report.py
#
# Exercise 2.4, 2.7, 2.9, 2.10, 2.11, 2.12

import csv
import sys
from typing import Tuple


def read_portfolio(filename: str) -> list[dict]:
    """Reads a csv at location filename. Requires csv file to contain headers
    named 'name', 'shares', and 'price'."""
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        return [{'name': dict(zip(headers, row))['name'],
                 'shares': int(dict(zip(headers, row))['shares']),
                 'price': float(dict(zip(headers, row))['price'])}
                for row in rows]


def parse_csv(filename: str) -> list[dict]:
    """Reads csv at location filename. Requires csv file to contain headers on first line.
    Returns the rows of the csv as a list of dictionaries in which keys are column headers
    and values are cell values, which are coerced into int, float, or str type."""
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        return [{header: coerce(value)
                 for header, value in zip(headers, row)}
                for row in rows]


def coerce(s):
    """Helper function for type coercion"""
    try:
        if s.isnumeric():
            return int(s)

        return float(s)

    except ValueError:
        return s


def read_prices(filename: str) -> dict:
    """Reads a csv at location filename
    Returns a dict with k:v pairs being values from two columns"""
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        return {row[0]: float(row[1])
                for row in rows
                if len(row) >= 2}


def make_report(portfolio, prices) -> list:
    """
    Given a list of dict, portfolio, containing portfolio info, and a dict of prices
    Returns a list of tuples of len 4 with indices Name, Shares, Price, Change
    """
    return [(stock['name'],
             stock['shares'],
             prices[stock['name']],  # Current Price
             prices[stock['name']] - stock['price'])  # Change
            for stock in portfolio]


def run_report():
    """Solution to 2.4"""
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    for stock in portfolio:
        name, shares, price = stock['name'], stock['shares'], stock['price']
        if name not in prices:
            print(f'Could not find current price for stock {name}')
            continue
        margin = prices[name] - stock['price']
        gain_loss = 'Gained' if margin >= 0 else 'Lost'
        total_margin = abs(margin * shares)

        print(f'Stock: {name}')
        print(f'{gain_loss}: ${total_margin:.2f} ')


def print_report(report):
    """Solution to 3.1/3.2"""
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        str_price = "$" + str(price).format('.2f')
        print(f'{name:>10s} {shares:>10d} {str_price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename) -> None:
    """Solution to 2.9 / 3.1"""
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    main(sys.argv)
