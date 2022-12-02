#!/usr/bin/env python3

# the function interleave, returns one list containing all the elements from the input lists interleaved

def interleave(*lists):
    ret = []
    zip_list = list(zip(*lists))
    for x in zip_list:
        ret.extend(x)
    return ret

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
