string = '         '
dash = '-' * 9

grid = [[string[0], string[1], string[2]], [string[3], string[4], string[5]], [string[6], string[7], string[8]]]

def board():

    grid = [[string[0], string[1], string[2]], [string[3], string[4], string[5]], [string[6], string[7], string[8]]]
    print(dash)
    for row in grid:
        s = '| {0} {1} {2} |'.format(row[0], row[1], row[2])
        print(s)
    print(dash)
board()

coordsdict = {
    "1 1": 6, "1 2": 3, "1 3": 0,
    "2 1": 7, "2 2": 4, "2 3": 1,
    "3 1": 8, "3 2": 5, "3 3": 2
}


winO = ['OOO']
winX = ['XXX']
game = True
while game == True:
    stringx = 'X'
    stringy = 'O'
    stringempty2 = ' '

    winningcombos = [[string[0] + string[1] + string[2]],
                [string[0] + string[3] + string[6]],
                [string[0] + string[4] + string[8]],
                [string[3] + string[4] + string[5]],
                [string[6] + string[7] + string[8]],
                [string[2] + string[4] + string[6]],
                [string[1] + string[4] + string[7]],
                [string[2] + string[5] + string[8]]]

    if winX in winningcombos:
        print("X wins")
        break
    elif winO in winningcombos:
        print("O wins")
        break
    elif stringempty2 not in string:
        print("Draw")
        break

    coordinates = input("Enter the coordinates: ")
    try:
        c = int(coordinates[0])
    except ValueError:
        print("You should enter numbers!")
        continue
    c1 = int(coordinates[0])
    c2 = int(coordinates[2])
    if (c1 < 1) or (c1 > 3):
        print("Coordinates should be from 1 to 3!")
    elif (c2 < 1) or (c2 > 3):
        print("Coordinates should be from 1 to 3!")
    elif coordinates in coordsdict:
        move = coordsdict[coordinates]
        if string[move] != ' ':
            print("This cell is occupied! Choose another one!")
        elif string.count(stringx) == 0:
            string = string[:move] + "X" + string[move+1:]
            board()
        elif string.count(stringx) > string.count(stringy):
            string = string[:move] + "O" + string[move+1:]
            board()
        else:
            string = string[:move] + "X" + string[move+1:]
            board()
