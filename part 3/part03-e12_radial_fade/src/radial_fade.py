#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    """Returns the center of the image 'a'.in order (center_y, center_x)"""
    return ((a.shape[0]-1)/2, (a.shape[1]-1)/2)

def radial_distance(a):
    ''' input is an image. output is an image where each pixel is replaced by the distance from the center of the image. '''
    height, width = a.shape[0], a.shape[1]
    y_center, x_center = center(a)
    y = np.full((width, height), range(height)).T
    x = np.full((height, width), range(width))
    return np.sqrt((y-y_center)**2 + (x-x_center)**2)


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range [tmin,tmax]."""

    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    ''' takes an image as a parameter and returns an array with same height and width filled with values between 0.0 and 1.0. '''
    image = a.copy()
    return scale(1- radial_distance(image))

def radial_fade(a):
    ''' takes an image as a parameter and returns an image multiplied by its radial mask.'''
    return  a * radial_mask(a)[:, :, np.newaxis]

def main():
    x = plt.imread('src/painting.png')
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(x)
    ax[1].imshow(radial_mask(x))
    ax[2].imshow(radial_fade(x))
    plt.show()

if __name__ == "__main__":
    main()
