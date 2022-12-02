#!/usr/bin/env python3

import math

# Main asks the user for a shape (triangle, rectangle, circle) 
# and its dimensions and then prints the area of the shape.

# exeptions:
#   An empty string as input will exit the loop. 
#   If the user gives a string that is none of the given shapes, 
#   the message “Unknown shape!” should be printed. 

def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle":
            a = float(input("Give base of the triangle: "))
            b = float(input("Give height of the triangle: "))
            print(f"The area is {a * b / 2}")
        elif shape == "rectangle":
            a = float(input("Give width of the rectangle: "))
            b = float(input("Give height of the rectangle: "))
            print(f"The area is {a * b}")
        elif shape == "circle":
            a = float(input("Give radius of the circle: "))
            print(f"The area is {a ** 2 * math.pi}")
        else:
            print("Unknown shape!")

    


if __name__ == "__main__":
    main()
