#!/usr/bin/env python3

import sys

def file_count(filename):
    """Count the number of lines, words, and characters in a file. Return a tuple containing the counts."""
    with open(filename) as f:
        lines = 0
        words = 0
        characters = 0
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
        return lines, words, characters

def main():
    """The main function calls the function file_count for each filename in the list sys.argv[1:] of command line parameters. """
    for filename in sys.argv[1:]:
        x = file_count(filename)
        print(f'{x[0]}\t{x[1]}\t{x[2]}\t{filename}')

if __name__ == "__main__":
    main()
