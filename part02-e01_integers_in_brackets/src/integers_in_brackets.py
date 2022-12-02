#!/usr/bin/env python3
import re

# the integers_in_brackets function finds all integers that are enclosed in brackets from a given string. there can be whitespace between the number and the brackets, but no other character besides those that make up the integer.
def integers_in_brackets(s):
    return [int(i) for i in re.findall(r"\[\s*([+-]?\d+)\s*\]", s)]

def main():
    print(integers_in_brackets("afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx") )
    # returns [12, -43, 12]

if __name__ == "__main__":
    main()