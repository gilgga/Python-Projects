#
# Game of Life
#


import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

# A = createBoard(5,3)
# print(A)


import sys

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
# A = createBoard(5,3)
# printBoard(A)


def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

A = diagonalize(7,7)
print(A)
printBoard(A)


def innerCells(w,h):
    A = createBoard( w, h )

    for row in range(1, h-1):
        for col in range(1, w-1):
            if row == col:
                A[row][col] = 1
            elif row > col or col > row:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

# A = innerCells(5,5)
# printBoard(A)


def randomCells(w,h):
    A = createBoard( w, h )

    for row in range(1, h-1):
        for col in range(1, w-1):
            if row == col:
                A[row][col] = random.choice([0,1])
            elif row > col or col > row:
                A[row][col] = random.choice([0,1])
            else:
                A[row][col] = 0
    return A

# A = randomCells(10,10)
# printBoard(A)


# oldA = createBoard(2,2)
# printBoard(oldA)
#  
# newA = oldA
# print(newA)
# printBoard(newA)
# 
# oldA[0][0] = 1
# printBoard(oldA)
# 
# printBoard(newA)


def copy(A):
    """Creates a deep copy of the input grid A"""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)
    for row in range(1, height-1):
        for col in range(1, width-1):
            newA.append(A[row][col])
    return newA


# oldA = createBoard(2,2)
# printBoard(oldA)
#  
# newA = copy(oldA)
# # print(newA)
# printBoard(newA)
#   
# oldA[0][0] = 1
# printBoard(oldA)
#  
# printBoard(newA)


def innerReverse(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height-1):
        for col in range(1, width-1):
            if A[row][col] == 1:
                newA[row][col] = 0
            else:
                newA[row][col] = 1
    return newA

# A = randomCells(8,8)
# printBoard(A)
# 
# A2 = innerReverse(A)
# printBoard(A2)


def countNeighbors(row, col, A):
    """Returns the number of live neighbors for a cell in the board
    A at a particular row and col"""
    count = 0
    if A[row-1][col-1] == 1:
        count += 1
    if A[row-1][col] == 1:
        count += 1
    if A[row-1][col+1] == 1: 
        count += 1
    if A[row][col-1] == 1:  
        count += 1
    if A[row][col+1] == 1:
        count += 1
    if A[row+1][col-1] == 1:
        count += 1
    if A[row+1][col] == 1: 
        count += 1
    if A[row+1][col+1] == 1:
        count += 1
    return count

# sampleA = [[0,0,0,0,0],
#            [0,0,1,0,0],
#            [0,0,1,0,0],
#            [0,0,1,0,0],
#            [0,0,0,0,0]]
# print(countNeighbors(1, 2, sampleA))
# print(countNeighbors(2, 2, sampleA))
# print(countNeighbors(3, 2, sampleA))
    
def next_life_generation(A):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)
    
    for row in range(1, height-1):
        for col in range(1, width-1):
            if countNeighbors(row, col, A) < 2:
                newA[row][col] = 0 
            elif countNeighbors(row, col, A) > 3:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) == 3 and A[row][col] == 0:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA                
 
A = [ [0,0,0,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,1,0,0],
 [0,0,0,0,0]]
  
printBoard(A)
  
A2 = next_life_generation( A )
printBoard(A2)
  
A3 = next_life_generation( A2 )
printBoard(A3)
