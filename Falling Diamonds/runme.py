#!/usr/bin/env python3
"""
Falling Diamonds problem
for Google Code Jam 2013
Round 1B

Link to problem description:
https://code.google.com/codejam/contest/2434486/dashboard#s=p1

author: 
Chris Nitsas
(nitsas)

language:
Python 3.2.3

date:
May, 2012

usage:
$ python3 runme.py sample.in
or
$ runme.py sample.in
(where sample.in is the input file and $ the prompt)
"""


import sys
from math import factorial
from operator import mul
# non-standard modules:
from helpful import read_int, read_list_of_int


def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def number_of_diamonds_in_pyramid_with_top_at(x, y):
    return int((y + 1) * (y + 2) / 2)
        

def probability_that_we_get_a_diamond(n, x, y):
    # abs(x) + y must be even for a diamond's center to land there
    if (abs(x) + y) % 2 != 0:
        # no diamond's center will land on x, y
        return 0.0
    elif x == 0:
        Dlow = number_of_diamonds_in_pyramid_with_top_at(x, y)
        if n >= Dlow:
            return 1.0
        else:
            return 0.0
    else:
        pyramid = number_of_diamonds_in_pyramid_with_top_at(0, abs(x) + y - 2)
        Dlow = pyramid + y + 1
        Dhigh = pyramid + abs(x) + 2 * y + 1
        if n < Dlow:
            return 0.0
        elif n >= Dhigh:
            return 1.0
        else:
            # Dlow <= n <= (Dhigh - 1)
            left = n - pyramid
            # I thought it should be
            # range(y + 1, min(left + 1, abs(x) + y + 1)) but that's wrong
            return float(sum( (binomial_coefficient(left, i) * (0.5 ** left)) for i in range(y + 1, left + 1) ))


def main(filename=None):
    if filename is None:
        if len(sys.argv) == 2:
            filename = sys.argv[1]
        else:
            print("Usage: runme.py input_file")
            return 1
    with open(filename, "r") as f:
        num_test_cases = read_int(f)
        for i in range(1, num_test_cases + 1):
            n, x, y = read_list_of_int(f)
            print("Case #{0}:".format(i), end=" ")
            print(probability_that_we_get_a_diamond(n, x, y))
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)

