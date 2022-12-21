#!/usr/bin/env python3

# the function distinct_characters takes a list of strings as a parameter.
# I then returns a dictionary where the keys are the words in the list and
# the values are the number of distinct characters in the word.

def distinct_characters(L):
    ret ={}
    for x in L:
        ret[x] = len(set(x))
    return ret

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
