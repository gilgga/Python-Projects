'''
Created on Dec 4, 2017

@author: austr
'''

class Board(object):
    
    def __init__(self, width=7, height=6):
        self.__width = width
        self.__height = height
        board = self.createBoard(self.__width, self.__height)
        self.__board = board
        
    def createOneRow(self, width):
        """Returns one row of zeros of width "width"...  
           You should use this in your
           createBoard(width, height) function."""
        row = []
        for col in range(width):
            row += [" "]
        return row

    def createBoard(self, width, height):
        """ returns a 2d array with "height" rows and "width" cols """
        A = []
        for row in range(height):
            A += [self.createOneRow(width)] # What do you need to add a whole row here?
        return A    
                
                
    def allowsMove(self, col):
        if col > self.__width:
            return False
        if self.__board[0][col] == " ":
            return True
        else:
            return False
    
    
    def addMove(self, col, ox):
        index_of_placement = -1
        for row in range(self.__height):
            if self.__board[row][col] == " ":
                index_of_placement += 1
            else:
                break
        self.__board[index_of_placement][col] = ox
    
    
    def setBoard(self, move_string):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in move_string:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
    
    
    def delMove(self, col):
        for row in range(self.__height):
            if self.__board[row][col] == " ":
                continue
            else:
                self.__board[row][col] = " "     
            
    
    def winsFor(self, ox):
        """Need to use a bunch of for loops"""
        for row in range(self.__height - 3):    #Vertical Downwards
            for col in range(self.__width):
                if self.__board[row][col] == ox and self.__board[row+1][col] == ox and self.__board[row+2][col] == ox and self.__board[row+3][col] == ox:
                    return True
         
        for row in range(self.__height):    #Horizontal Right
            for col in range(self.__width - 3):
                if self.__board[row][col] == ox and self.__board[row][col+1] == ox and self.__board[row][col+2] == ox and self.__board[row][col+3] == ox:
                    return True
        
        for row in range(3, self.__height):    #Up to the Right
            for col in range(self.__width - 3):
                if self.__board[row][col] == ox and self.__board[row-1][col+1] == ox and self.__board[row-2][col+2] == ox and self.__board[row-3][col+3] == ox:
                    return True
                
        for row in range(self.__height - 3):    #Down and to the Right
            for col in range(self.__width - 3):
                if self.__board[row][col] == ox and self.__board[row+1][col+1] == ox and self.__board[row+2][col+2] == ox and self.__board[row+3][col+3] == ox:
                    return True
        
        return False
    
    
    def hostGame(self):
        turn = "X"
        print("Welcome to Connect Four!")
        lst = []
        for i in range(self.__width):
            lst.append(str(i))
        #print(lst)
        while True:
            print("")
            print(self)
            print("")
            turn = "X"
            x = input("X's choice:  ")
            while x not in lst or not self.allowsMove(int(x)):
                x = input("Error, you need to enter a valid input: ")
            x=int(x)
            self.addMove(x, turn)
            if self.winsFor("X"):
                print("")
                print("")
                print("X wins -- Congratulations!")
                print("")
                print(self)
                break
            turn = "O"
            print("")
            print(self)
            print("")
            x = input("O's choice:  ")
            while x not in lst or not self.allowsMove(int(x)):
                x = input("Error, you need to enter a valid input: ")
            x=int(x)
            self.addMove(x, turn)
            
            if self.winsFor("O"):
                print("")
                print("")
                print("O wins -- Congratulations!")
                print("")
                print(self)
                break
            
    
    def __str__(self):
        """Pipe characters in between characters of 2D array
        End of row has it too
        End of array print dashes
        Need 
        Need accumulator string"""
        newboard = ""
        num_row = len(self.__board)
        for row in range(num_row):
            num_cols = len(self.__board[row])
            for col in range(num_cols):
                newboard += "|"
                newboard += self.__board[row][col]
            newboard += "|"
            newboard += "\n"
        dashes = "-"*self.__width*2 + "-"
        newboard += dashes
        newboard += "\n"
        num_label = 0
        for number in range(self.__height + 1):
            newboard += " "
            newboard += str(num_label)
            num_label += 1
        return str(newboard)
    

# if __name__ == "__main__":
#     b = Board(7,6)
#     b.setBoard("12233434464")   #Diagonal Upa nd to the Right
#     print(b)
#     print(b.winsFor("X"))
#     b.setBoard("121211123334")    #Diagonal Down and to the Left
#     print(b)
#     print(b.winsFor("O"))
#     b.hostGame()
#     b.setBoard("11223345")  #Horizontal
#     print(b)
#     print(b.winsFor("X"))
#     b.setBoard("12121213")  #Vertical
#     print(b)
#     print(b.winsFor("X"))
#     b.hostGame()