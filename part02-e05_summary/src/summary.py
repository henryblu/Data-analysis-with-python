#!/usr/bin/env python3

import sys

#summary gets a filename as a parameter. The input file should contain a floating point number on each line of the file. Make your function read these numbers and then return a triple containing the sum, average, and standard deviation of these numbers for the file.

def std(numbers):
    """Calculate the standard deviation of a list of numbers."""
    average = sum(numbers)/len(numbers)
    return (sum([(x-average)**2 for x in numbers])/len(numbers))**0.5

def summary(filename):
    '''
    # summary gets a filename as a parameter. 
    # The input file should contain a floating point number on each line of the file. 
    # summary reads these numbers and then return a triple containing the sum, average, and standard deviation of these numbers for the file.
    '''

    with open(filename) as f:
        numbers = []
        for line in f:
            try :
                numbers.append(float(line))
            except ValueError:
                pass
        ret = f"File: {filename} Sum: {round(sum(numbers), 6)} Average: {round(sum(numbers)/len(numbers),6)} Standard Deviation: {round(std(numbers),6)}"
        return ret

def main():
    """The main function calls the function summary for each filename in the list sys.argv[1:] of command line parameters. """
    for filename in sys.argv[1:]:
        print(summary(filename))

if __name__ == "__main__":
    main()
