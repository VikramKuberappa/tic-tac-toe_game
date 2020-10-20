import os

grid = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def grid_print():
    print(grid[0][0],grid[0][1],grid[0][2])
    print(grid[1][0],grid[1][1],grid[1][2])
    print(grid[2][0],grid[2][1],grid[2][2])


def grid_update(r,c,player):
    grid[r][c]=player

os.system('cls')
itr=0
while itr<=9:
    if grid[0][0]==grid[0][1]==grid[0][2]=="V" or grid[1][0]==grid[1][1]==grid[1][2]=="V" or grid[2][0]==grid[2][1]==grid[2][2]=="V" or grid[0][0]==grid[1][0]==grid[2][0]=="V" or grid[0][1]==grid[1][1]==grid[2][1]=="V" or grid[0][2]==grid[1][2]==grid[2][2]=="V" or grid[0][0]==grid[1][1]==grid[2][2]=="V" or grid[0][2]==grid[1][1]==grid[2][0]=="V" :
        print(" Vikram Won the game")
        break
    elif grid[0][0]==grid[0][1]==grid[0][2]=="S" or grid[1][0]==grid[1][1]==grid[1][2]=="S" or grid[2][0]==grid[2][1]==grid[2][2]=="S" or grid[0][0]==grid[1][0]==grid[2][0]=="S" or grid[0][1]==grid[1][1]==grid[2][1]=="S" or grid[0][2]==grid[1][2]==grid[2][2]=="S" or grid[0][0]==grid[1][1]==grid[2][2]=="S" or grid[0][2]==grid[1][1]==grid[2][0]=="S" :
        print("Shivu won the game")
        break
    elif itr==9:
        print("Match Tie")
        break
    else:
        if itr%2==0:
            print("It's S Turn")
            r=int(input("enter row: "))
            c=int(input("enter column: "))
            player="S"
        else:
            print("It's V Turn")
            r=int(input("enter row"))
            c=int(input("enter column"))
            player="V"
        if grid[r][c]=="-":
            grid_update(r,c,player)
            os.system('cls')
            grid_print()
            itr+=1
        else:
            print("Input exist")
