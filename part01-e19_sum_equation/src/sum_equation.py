#!/usr/bin/env python3

# the function sum_equation returns a string that represents the sum of the numbers in the list
def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    return ' + '.join(map(str, L)) + ' = ' + str(sum(L))


def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
