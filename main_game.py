#imports
#-------------------------------------------------------------------/
import random
import sys

#variables
#-------------------------------------------------------------------/
playingGrid = [
    [0,0,0,0], #This row is simply padding to make the coordinates work better
    [0,1,0,0],
    [0,1,0,0],
    [0,1,0,0]
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
#  11  21  31
#  12  22  32
#  13  23  33
#  11  12  13
#  21  22  23
#  31  32  33
#  11  22  33
#  13  22  31

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

def checkForWinner():
    for i in range(1, 4):
        for j in range(1, 4):
            
            if printGrid[i][j] == 0:
                continue






        
checkForWinner














#main game
#----------------------------------------------------------------/
#instructions

#  _ _ _ _ _ _ _ _ Y
#|    1   2   3   
#|   ┌ ─ ┬ ─ ┬ ─ ┐ 
#| 1 │ X │   │   │ 
#|   ├ ─ ┼ ─ ┼ ─ ┤ 
#| 2 │ X │   │   │ 
#|   ├ ─ ┼ ─ ┼ ─ ┤ 
#| 3 │ X │   │   │ 
#|   └ ─ ┴ ─ ┴ ─ ┘ 
#X