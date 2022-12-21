#!/usr/bin/env python3

# the function merge merges two sorted lists into one 
# sorted list by iterating though each list.
def merge(L1, L2):
    L3 = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i += 1
        else:
            L3.append(L2[j])
            j += 1
    
    # now append the remaining elements of L1 or L2
    if i == len(L1):
        L3.extend(L2[j:])
    else:
        L3.extend(L1[i:])
    return L3
    

def main():
    pass

if __name__ == "__main__":
    main()
