#!/usr/bin/env python3

# the function acronyms returns a list of acronyms from a string
# the rules that define an acronym are:
# - the acronym must be at least 2 characters long
# - the acronym must be all uppercase
import string

def acronyms(s):
    return list(filter(lambda x: len(x) > 1 and x.isupper(), map(lambda x: x.translate(str.maketrans('', '', string.punctuation)), s.split())))

def main():
    print(acronyms("""For the purposes of the EU General Data Protection Regulation (GDPR), the controller of your personal information is International Business Machines Corporation (IBM Corp.), 1 New Orchard Road, Armonk, New York, United States, unless indicated otherwise. Where IBM Corp. or a subsidiary it controls (not established in the European Economic Area (EEA)) is required to appoint a legal representative in the EEA, the representative for all such cases is IBM United Kingdom Limited, PO Box 41, North Harbour, Portsmouth, Hampshire, United Kingdom PO6 3AU."""))


if __name__ == "__main__":
    main()
