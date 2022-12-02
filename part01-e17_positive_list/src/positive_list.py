#!/usr/bin/env python3

# the positive_list function filters out all none positive numbers from a list 
def positive_list(L):
    return list(filter(lambda x: x > 0, L))

def main():
    print(positive_list([2,-2,0,1,-7])) 

if __name__ == "__main__":
    main()
