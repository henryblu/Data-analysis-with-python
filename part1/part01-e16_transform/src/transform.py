#!/usr/bin/env python3
# transfor takes two strings with integers and multiplys each integer in
# the first string with the corresponding integer in the second string. 
def transform(s1, s2):
    l = list(zip(s1.split(), s2.split()))
    return list(map(lambda x: int(x[0]) * int(x[1]), l))


def main():
    print (transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
