#!/usr/bin/env python3

# this main function iterates thorugh all possible combinations of two dice and prints all combinations that sum to 5
def main():
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == 5:
                print(f"({i},{j})")

if __name__ == "__main__":
    main()
