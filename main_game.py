#imports
#-------------------------------------------------------------------/
import random
import sys
import time
import collections, itertools

#variables
#-------------------------------------------------------------------/
playingGrid = [
    [0,0,0,0], #This row is simply padding to make the coordinates work better
    [0,0,1,0],
    [0,0,0,0],
    [0,0,0,0]
]



#grid layout
#------------------------------------------------------------------/
def coorToText(num):
    if num == 0: 
        return ' ' #returns nothing to show the grid space as empty
    if num == 1:
        return 'O' #add 1 to the value to make a O
    if num == 2:
        return 'X' #add 2 to the value to make a X


def printGrid():
    print('    1   2   3   ')
    print('  ┌ ─ ┬ ─ ┬ ─ ┐ ')
    print('1 │ ' + coorToText(playingGrid[1][1]) + ' │ ' + coorToText(playingGrid[1][2]) + ' │ ' + coorToText(playingGrid[1][3]) + ' │')
    print('  ├ ─ ┼ ─ ┼ ─ ┤ ')
    print('2 │ ' + coorToText(playingGrid[2][1]) + ' │ ' + coorToText(playingGrid[2][2]) + ' │ ' + coorToText(playingGrid[2][3]) + ' │')
    print('  ├ ─ ┼ ─ ┼ ─ ┤ ')
    print('3 │ ' + coorToText(playingGrid[3][1]) + ' │ ' + coorToText(playingGrid[3][2]) + ' │ ' + coorToText(playingGrid[3][3]) + ' │')
    print('  └ ─ ┴ ─ ┴ ─ ┘ ')



#check winner
#-----------------------------------------------------------------/

#winning combos
#  11  21  31 - H
#  12  22  32 - H
#  13  23  33 - H
#  11  12  13 - V
#  21  22  23 - V
#  31  32  33 - V
#  11  22  33 - MD
#  13  22  31 - SD

#|   11  21  31   |      12  22  32   |      13  23  33   |      11  12  13   |      21  22  23   |      31  32  33   |      11  22  33   |      13  22  31  
#|----------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|------------------
#|    1   2   3   |       1   2   3   |       1   2   3   |       1   2   3   |       1   2   3   |       1   2   3   |       1   2   3   |       1   2   3  
#|  ┌ ─ ┬ ─ ┬ ─ ┐ |     ┌ ─ ┬ ─ ┬ ─ ┐ |     ┌ ─ ┬ ─ ┬ ─ ┐ |     ┌ ─ ┬ ─ ┬ ─ ┐ |     ┌ ─ ┬ ─ ┬ ─ ┐ |     ┌ ─ ┬ ─ ┬ ─ ┐ |     ┌ ─ ┬ ─ ┬ ─ ┐ |     ┌ ─ ┬ ─ ┬ ─ ┐
#|1 │ X │   │   │ |   1 │   │ X │   │ |   1 │   │   │ X │ |   1 │ X │ X │ X │ |   1 │   │   │   │ |   1 │   │   │   │ |   1 │ X │   │   │ |   1 │   │   │ X │
#|  ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤
#|2 │ X │   │   │ |   2 │   │ X │   │ |   2 │   │   │ X │ |   2 │   │   │   │ |   2 │ X │ X │ X │ |   2 │   │   │   │ |   2 │   │ X │   │ |   2 │   │ X │   │
#|  ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤ |     ├ ─ ┼ ─ ┼ ─ ┤
#|3 │ X │   │   │ |   3 │   │ X │   │ |   3 │   │   │ X │ |   3 │   │   │   │ |   3 │   │   │   │ |   3 │ X │ X │ X │ |   3 │   │   │ X │ |   3 │ X │   │   │
#|  └ ─ ┴ ─ ┴ ─ ┘ |     └ ─ ┴ ─ ┴ ─ ┘ |     └ ─ ┴ ─ ┴ ─ ┘ |     └ ─ ┴ ─ ┴ ─ ┘ |     └ ─ ┴ ─ ┴ ─ ┘ |     └ ─ ┴ ─ ┴ ─ ┘ |     └ ─ ┴ ─ ┴ ─ ┘ |     └ ─ ┴ ─ ┴ ─ ┘

def checkForWinner(x, y):

    #check if previous move caused a win on vertical line 
    if playingGrid[1][y] == playingGrid[2][y] == playingGrid [3][y]:
        return True

    #check if previous move caused a win on horizontal line 
    if playingGrid[x][1] == playingGrid[x][2] == playingGrid [x][3]:
        return True

    #check if previous move was on the main diagonal and caused a win
    if x == y and playingGrid[1][1] == playingGrid[2][2] == playingGrid [3][3]:
        return True

    #check if previous move was on the secondary diagonal and caused a win
    if x + y == 3 and playingGrid[1][3] == playingGrid[2][2] == playingGrid [3][1]:
        return True

    return False 



#main game
#----------------------------------------------------------------/
#instructions

# input('Hello! Welcome to Noughts and Crosses. Please decide who is Player 1 and who is Player 2 now. Hit enter when decided.')
# print('')
# print('Ok, here are the rules. Player 1 you are Noughts (O) and Player 2 you are Crosses (X). Noughts will go first everytime so I suggest if you play again you Rock, Paper, Scissors, for who that is.')
# print('')
# print('The way you mark the board is with coordinates along the X and Y axis. An example is 1 1 this will be square 1 on the board and 2 3 will be the third in the middle row like shown below.')
# print('Its the Y axis followed by the X axis.')
# print('  _ _ _ _ _ _ _ _ X')
# print('|    1   2   3   ')
# print('|   ┌ ─ ┬ ─ ┬ ─ ┐ ')
# print('| 1 │ O │   │   │ ')
# print('|   ├ ─ ┼ ─ ┼ ─ ┤ ')
# print('| 2 │   │   │ X │ ')
# print('|   ├ ─ ┼ ─ ┼ ─ ┤ ')
# print('| 3 │   │   │   │ ')
# print('|   └ ─ ┴ ─ ┴ ─ ┘ ')
# print('Y')

def playerXMove():
    freq = collections.defaultdict(int) #This counts how many 1's and 2's are on the board. 
    for x in itertools.chain.from_iterable(playingGrid):
        freq[x] += 1
    
    if freq[1] > freq[2]:
        return True   #if O is larger than X return True so X goes next.
    if freq[1] == freq[2]:
        return False  #if O is equel to X then O goes next. 

    return 
        

playerXMove()


time.sleep(5)
sys.exit
