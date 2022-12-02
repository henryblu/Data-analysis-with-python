#!/usr/bin/env python3

import re

# the function file_listing loads the file src/listing.txt and returns a list of tuples (size (int), month, day, hour, minute, filename). 
def file_listing(filename="src/listing.txt"):
    with open(filename, "r") as f:
        return [(int(i[0]), i[1], int(i[2]), int(i[3]), int(i[4]), i[5]) for i in re.findall(r"(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(.+)", f.read())]


def main():
    print(file_listing())

if __name__ == "__main__":
    main()
