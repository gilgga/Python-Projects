'''
Created on Oct 2, 2017

@author: austr

'''

def list_build(lst):   #Building the list
    """Adds every pair of consecutive terms"""
    if lst == []:
        return []
    if len(lst) == 1:
        return []
    return [lst[0] + lst[1]] + list_build(lst[1:])
    
def pascal_row(n):
    """Takes as input a single integer n greater than or equal to 0.  Returns a list of elements found in a certain row of Pascal's Triangle."""
    def pascal_row_help(n, row_counter, row): #Does list iteration
        if n < 0:
            return []
        if n == 0:
            return [1]
        if row_counter == n:
            return row
        return pascal_row_help(n, row_counter + 1, [1] + list_build(row) + [1])
    return pascal_row_help(n, 0, [])

#print(pascal_row(5))
#When writing code, think of it one operation at a time and do it sequentially

def pascal_triangle(n):
    """Takes as input a single integer n.  Returns a list of lists containing the values of all the rows up to and including row n"""
    if n < 0:
        return []
    if n == 0:
        return [[1]]
    return pascal_triangle(n-1) + [pascal_row(n)]

#print(pascal_triangle(5))

