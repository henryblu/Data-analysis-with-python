#!/usr/bin/env python3

# Function triple multiplies its parameter by three
def triple(x):
    return x * 3

# Function square squares its parameter
def square(x):
    return x * x

# Part 1: main function is a for loop that iterates through values 1 to 10, and for each value prints its triple and its square.
# Part 2: the main function stops iteration when the square of a value is larger than the triple of the value, without printing anything in the last iteration.
def main():
    for i in range(1, 11):
        sq_i = square(i)
        tr_i = triple(i)

        if sq_i > tr_i:
            break

        print(f'triple({i})=={tr_i} square({i})=={sq_i}')
        
    

if __name__ == "__main__":
    main()
