"triangle module"

__version__ = "1.0"

__author__ = "Henry Blue"

def hypothenuse(a, b):
    """the function hypothenuse returns the length of the hypothenuse of a right-angled triangle
    """
    return (a**2 + b**2)**0.5


def area(a, b):
    """the function area returns the area of a right-angled triangle
    """
    return a*b/2
