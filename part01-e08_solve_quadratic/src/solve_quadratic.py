#!/usr/bin/env python3

import math

# the function solve_quadratic returns both solutions of a generic 
# quadratic as a pair (2-tuple) when the coefficients are given as parameters.
def solve_quadratic(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

# main is in the program template but is not used in the exercise.
def main():
    pass

if __name__ == "__main__":
    main()
