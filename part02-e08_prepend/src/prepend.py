#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, string) -> None:
        '''This method initializes the class.'''
        self.string = string

    def write(self, text):
        '''This method writes text to stdout, prepending a string to each line.'''
        print(self.string + text)
        

def main():
    pass

if __name__ == "__main__":
    main()
