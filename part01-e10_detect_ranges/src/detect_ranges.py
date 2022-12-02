#!/usr/bin/env python3

# the function detect_range gets a list of integers as a parameter. 
# The function should then sort this list, and transform the list
# into another list where pairs are used for all the detected intervals. 
def detect_ranges(x):
    L= sorted(x)
    ret = []
    tmp = []
    for i in range(len(L)):
        if (i != len(L)-1) and (L[i+1] == L[i]+1):
                tmp.append(L[i])
        else:
            if L[i-1] == L[i]-1:
                ret.append((tmp[0],L[i]+1))
                tmp=[]
            else: 
                ret.append(L[i])
    return ret

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    L = [-2, 0, 1, 2, 3]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
