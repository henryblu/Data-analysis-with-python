#!/usr/bin/env python3
# the function reverse_dictionary takes in a dictionary of strings and returns the reverse of the dictionary. 
def reverse_dictionary(d):
    ret = {}
    for key, values in d.items():
        for value in values:
            if value not in ret:
                ret[value] = [key]
            else:
                ret[value].append(key)
    return ret

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)

if __name__ == "__main__":
    main()
