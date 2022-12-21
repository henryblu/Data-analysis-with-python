#!/usr/bin/env python3

class Rational(object):
    '''This class turns two integres into a rational number. it also has methods for adding, subtracting, multiplying, dividing, comparing and printing rational numbers.
    '''
    def __init__(self, x, y) -> None:
        '''This method initializes the class.'''
        self.x = x
        self.y = y
        self.rat= x/y

    def __add__(self, other):
        '''This method adds two rational numbers. and returns a rational type'''
        numerator = self.x * other.y + self.y * other.x
        denominator = self.y * other.y
        return Rational(numerator, denominator)
    def __sub__(self, other):    
        '''This method subtracts two rational numbers, and returns a rational type'''
        numerator = self.x * other.y - self.y * other.x
        denominator = self.y * other.y
        return Rational(numerator, denominator)
    def __mul__(self, other):
        '''This method multiplies two rational numbers and returns a rational type'''
        return Rational(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        '''This method divides two rational numbers and returns a rational type'''
        numerator = self.x * other.y
        denominator = self.y * other.x
        return Rational( numerator, denominator)
    def __gt__(self, other):
        '''This method compares two rational numbers '''
        return self.rat > other.rat
    def __le__(self, other):
        '''This method compares two rational numbers.'''
        return self.rat < other.rat
    def __eq__(self, other):
        '''This method compares two rational numbers.'''
        return self.rat == other.rat
    def __str__(self):
        '''This method returns a string representation of the rational number.'''
        return str(f'{self.x}/{self.y}')



def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1+r2)
    print((r1/r2)==Rational(3,8))

if __name__ == "__main__":
    main()
