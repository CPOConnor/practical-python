# sears.py
import math


def calc_nth_day_math(building_height: int, bill_thickness: float) -> int:
    """Mathematically calculate days using log to solve for n (442 = .11 * .001 * 2^(n-1) )
    Note that we are offsetting by 1 because day 1 refers to 1 bill or 2^0,
    day 2 refers to 2^1, and so on"""
    return math.ceil(math.log2(building_height / bill_thickness)) + 1


def calc_nth_day_iterative(building_height: int, bill_thickness: float) -> int:
    num_bills = 1
    day = 1
    while num_bills * bill_thickness < building_height:
        print(day, num_bills, num_bills * bill_thickness)
        day += 1
        num_bills = num_bills * 2
    return day


def print_stats(day: int, n_bills: int, bill_thickness: float) -> None:
    print('Number of days', day)
    print('Number of bills', n_bills)
    print('Final height', n_bills * bill_thickness)


dollar_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)

print("Math solution: ")
day_math_solution = calc_nth_day_math(sears_height, dollar_thickness)
print_stats(day_math_solution, 2 ** (day_math_solution - 1), dollar_thickness)  # Number of bills = 2^( n - 1 ) where n = # of days

print("Iterative solution:")
day_iter_solution = calc_nth_day_iterative(sears_height, dollar_thickness)
print_stats(day_math_solution, 2 ** (day_math_solution - 1), dollar_thickness)  # Number of bills = 2^( n - 1 ) where n = # of days

