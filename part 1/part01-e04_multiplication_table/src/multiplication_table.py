#!/usr/bin/env python3

# the main function prints out a multiplication table for the numbers 1 to 10
def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print("{:4}".format(i * j), end="")
        print()


if __name__ == "__main__":
    main()
