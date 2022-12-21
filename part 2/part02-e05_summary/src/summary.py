#!/usr/bin/env python3

import sys

#summary gets a filename as a parameter. The input file should contain a floating point number on each line of the file. Make your function read these numbers and then return a triple containing the sum, average, and standard deviation of these numbers for the file.

def std(numbers):
    """Calculate the standard deviation of a list of numbers."""
    average = sum(numbers)/len(numbers)
    sum_of_squares = 0
    for number in numbers:
        sum_of_squares += (number - average)**2
    return (sum_of_squares/(len(numbers)-1))**0.5

def summary(filename):
    """Read the file and return a triple containing the sum, average, and standard deviation of the numbers in the file."""

    with open(filename) as f:
        numbers = []
        for line in f:
            try :
                numbers.append(float(line))
            except ValueError:
                print(f"Invalid value in file {filename}: {line}")
        ret = sum(numbers), sum(numbers)/len(numbers), std(numbers)
        return ret

def main():
    """The main function calls the function summary for each filename in the list sys.argv[1:] of command line parameters. """
    for filename in sys.argv[1:]:
        x = summary(filename)
        print(f"File: {filename} Sum: {format(x[0], '.6f')} Average: {format(x[1], '.6f')} Stddev: {format(x[2], '.6f')}")

if __name__ == "__main__":
    main()
