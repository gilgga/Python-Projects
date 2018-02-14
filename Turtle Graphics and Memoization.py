'''
Created on 10/11/2017
@author:   Gil Gerard G. Austria

'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    """Returns a fractal tree with an initial trunk length of trunk_length and 4 sub branch levels"""
    subtractor = trunk_length/levels
    turtle.bgcolor("sky blue")
    turtle.pensize(10)
    turtle.penup()
    turtle.setposition(0,-200)
    turtle.left(90)
    turtle.color("brown")
    turtle.pendown()
    def sv_tree_helper(trunk_length, levels):
        pos = turtle.position()
        if trunk_length > 0:
            turtle.forward(trunk_length)
            turtle.right(30)
            sv_tree_helper(trunk_length-subtractor, levels)
            turtle.left(60)
            sv_tree_helper(trunk_length-subtractor, levels)
            turtle.right(30)
            turtle.backward(trunk_length)
        if pos == (0, -200):
            turtle.done()
        
    sv_tree_helper(trunk_length, levels)        


def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fast_lucas_helper(n, memo):
        if n in memo:       #Step 1: If this value is in the memo, return the associated value
            return memo[n]
        
        if n == 0:          #Step 2: Use recursion but store the value in another variable
            result = 2
        elif n == 1:
            result = 1
        else:       #Necessary because we're not returning values, we're assigning values
            result = fast_lucas_helper(n-1, memo) + fast_lucas_helper(n-2, memo)
        
        memo[n] = result    #Step 3: Put result in a memo and then return the result; n is the key for the dictionary
        return result
    return fast_lucas_helper(n, {})        #Encapsulating the helper function


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount,coins)]
        
        if amount < 0:
            result = float("inf")  
        elif coins == ():
            result = float("inf") 
        elif amount == 0:
            result = 0
        else:
            use_it = 1 + fast_change_helper(amount - coins[0], coins, memo)  
            lose_it = fast_change_helper(amount, coins[1:], memo)
            result = min(use_it, lose_it)
            
        memo[(amount, coins)] = result
        return result
    return fast_change_helper(amount, tuple(coins), {})     # Call the helper. Note we converted the list to a tuple.


print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100,4)
