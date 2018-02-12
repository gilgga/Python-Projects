# mandelbrot.py
# Lab 9
#
# Name:

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:

def mult(c,n):
    """mult uses only a loop and addition to multiply c by the integer n"""
    result = 0
    for x in range(n):
        result = result + c
    return result

# print(mult(6,7))
# print(mult(1.5,28))


def update(c,n):
    """Update starts with z=0 and runs z = z**2 + c for a total of n times.  It returns the final z"""
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

# print(update(1,3))
# print(update(-1,3))
# print(update(1,10))
# print(update(-1,10))


def inMSet(c,n):
    """inMSet takes in
            c for the update step of z = z**2 + c
            n, the maximum number of times to run that step
        Then, it should return
            False as soon as abs(z)>2
            True if abs(z) never gets larger than 2 (for n iterations)"""
    z = 0 + 0j
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

# c = 0 + 0j
# print(inMSet(c, 25))
# c = 3+4j
# print(inMSet(c, 25))
# c = 0.3+ -0.5j
# print(inMSet(c, 25))
# c = -0.7+0.3j
# print(inMSet(c, 25))
# c = 0.42+0.2j
# print(inMSet(c, 25))
# print(inMSet(c, 50))


def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col%10 == 0 or row%10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
     # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
    
# test()

"""Changing if col % 10 == 0 and row % 10 == 0: to the line if col % 10 == 0 or row % 10 == 0:
would couse the dots to turn into lines, so the image now looks like a grid."""


def scale(pix, pixMax, floatMin, floatMax):
    """Scale takes in
            pix, the CURRENT pixel column
            pixMax, the total # of pixel columns
            floatMin, the min floating-point value
            floatMax, the max floating-point value
        scale returns the floating-point value that
            corresponds to pix
    """
    return floatMin + (1.0*pix / pixMax)*(floatMax - floatMin)


# print(scale(100, 200, -2.0, 1.0))
# print(scale(100, 200, -1.5, 1.5))
# print(scale(100, 300, -2.0, 1.0))
# print(scale(25, 300, -2.0, 1.0))
# print(scale(299, 300, -2.0, 1.0))


def mset():
    """Creates a 300x200 image of the Mandelbrot set"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    
    # Create a loop in order to draw some pixels
    
    for col in range(width):
        for row in range(height):
        # here is where you will need
        # to create the complex number, c!
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y*1j
            n = 25
            if inMSet(c,n) == True:
                image.plotPoint(col,row)
    # we looped through every image pixel; we now write the file
    
    image.saveFile()
    
mset()
    