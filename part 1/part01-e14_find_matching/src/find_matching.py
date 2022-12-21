#!/usr/bin/env python3

# the function find_matching gets a list of strings and a search string as parameters
# it returns the indices to those elements in the input list that contain the search string.
def find_matching(L, pattern):
    ret =[]
    for i, x in enumerate(L):
        if pattern in x:
            ret.append(i)
    return ret

# mian function is in the template but not used in this exercise 
def main():
    pass

if __name__ == "__main__":
    main()
