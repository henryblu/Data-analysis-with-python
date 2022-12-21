#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    ''' input is a RGB image. output is a grayscale image. Useing the weights 0.2126, 0.7152, and 0.0722 for red, green, and blue, respectively. '''
    image = image.copy()
    return image[:, :, 0] * 0.2126 + image[:, :, 1] * 0.7152 + image[:, :, 2] * 0.0722

def to_red(image):
    ''' input is an RGB image. output is an image where the green and blue channels are set to zero. '''
    image = image.copy()
    image[:, :, (1,2)] = 0
    return image

def to_green(image):
    ''' input is an RGB image. output is an image where the red and blue channels are set to zero. '''
    image = image.copy()
    image[:, :, (0,2)] = 0
    return image

def to_blue(image):
    ''' input is an RGB image. output is an image where the red and green channels are set to zero. '''
    image = image.copy()
    image[:, :, (1,0)] = 0
    return image



def main():
    x = plt.imread('src/painting.png')
    plt.imshow(x)
    plt.show()
    grey = to_grayscale(x)
    red = to_red(x)
    blue = to_blue(x)
    green = to_green(x)

    fig,sub = plt.subplots(3,1)
    sub[0].imshow(red)
    sub[1].imshow(green)
    sub[2].imshow(blue)
    plt.show()


if __name__ == "__main__":
    main()
