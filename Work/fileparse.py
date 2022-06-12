# fileparse.py
#
# Exercise 3.3, 3.5, 3.7, 3.17
import csv
import sys
from pprint import pprint
from typing import TextIO


def parse_csv(file: object, selected_columns: list[str] = [],
              column_types: list[object] = [], has_headers: bool = True, delimiter=",") -> list:
    """Reads csv at location filename. Requires csv file to contain headers on first line.
    Returns the rows of the csv as a list of dictionaries in which keys are column headers
    and values are cell values, which are coerced into int, float, or str type."""
    if selected_columns and not has_headers:
        raise RuntimeError("Invalid arguments: cannot select columns without headers")
    if isinstance(file, str):
        raise RuntimeError("Invalid arguments: expected file, got string.")
    rows = csv.reader(file, delimiter=delimiter)
    if has_headers:
        headers = next(rows)
    # Pad column types with None values
    column_types = column_types + ((len(headers) - len(column_types)) * [None])
    return [{header: coerce(value, column_type)
             for header, value, column_type in zip(headers, row, column_types)
             if (header in selected_columns or not selected_columns)}
            for row in rows]


def coerce(s, column_type):
    """Helper function for type coercion"""
    # Attempt conversion from column_type argument
    try:
        if column_type:
            return column_type(s)
    except ValueError as e:
        print(f'WARNING: ValueError while attempting to parse {s} into type {column_type}')
        return None
    # Attempt conversion based on value, falling back to str if not int or float
    try:
        if s.isnumeric():
            return int(s)
        return float(s)
    except ValueError as e:
        return s


def main():
    with open('Data/missing.csv', 'rt') as file:
        d = parse_csv(file, selected_columns=['name', 'shares', 'price'], column_types=[str, int],
                      delimiter=',')
        pprint(d)


if __name__ == '__main__':
    main()

