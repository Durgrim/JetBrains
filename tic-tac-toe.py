'''
Tic-tac-toe game rules:

X Starts

Grid for user inputs:
(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)
(1, 1) (2, 1) (3, 1)

'''


cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print('---------')
print('| ' + str(cells[0][0]) + ' ' + str(cells[0][1]) + ' ' + str(cells[0][2]) + ' |')
print('| ' + str(cells[1][0]) + ' ' + str(cells[1][1]) + ' ' + str(cells[1][2]) + ' |')
print('| ' + str(cells[2][0]) + ' ' + str(cells[2][1]) + ' ' + str(cells[2][2]) + ' |')
print('---------')

x_num = 0
o_num = 0
turn = 0
while True:
    x, y = input('Enter the coordinates').split()
    if x not in '0123456789' or y not in '0123456789'or x == None or y == None:
        print("You should enter numbers!")
    elif int(x) > 3 or int(x) < 1 or int(y) < 1 or int(y) > 3:
        print("Coordinates should be from 1 to 3!")
    elif cells[3 - int(y)][int(x) - 1] == 'X' or cells[3 - int(y)][int(x) - 1] == 'O':
        print("This cell is occupied! Choose another one!")
    else:
        turn += 1
        if turn % 2 == 1:
            cells[3 - int(y)][int(x) - 1] = 'X'
            x_num += 1
        else:
            cells[3 - int(y)][int(x) - 1] = 'O'
            o_num += 1
            
        print('---------')
        print('| ' + str(cells[0][0]) + ' ' + str(cells[0][1]) + ' ' + str(cells[0][2]) + ' |')
        print('| ' + str(cells[1][0]) + ' ' + str(cells[1][1]) + ' ' + str(cells[1][2]) + ' |')
        print('| ' + str(cells[2][0]) + ' ' + str(cells[2][1]) + ' ' + str(cells[2][2]) + ' |')
        print('---------')
        
        xwin = False
        if (cells[0][0], cells[0][1], cells[0][2]) == ('X', 'X', 'X') or (cells[1][0], cells[1][1], cells[1][2]) == ('X', 'X', 'X') or (cells[2][0], cells[2][1], cells[2][2]) == ('X', 'X', 'X') \
        or (cells[0][0], cells[1][0], cells[2][0]) == ('X', 'X', 'X') or (cells[0][1], cells[1][1], cells[2][1]) == ('X', 'X', 'X') or (cells[0][2], cells[1][2], cells[2][2]) == ('X', 'X', 'X') \
        or (cells[0][0], cells[1][1], cells[2][2]) == ('X', 'X', 'X') or (cells[0][2], cells[1][1], cells[2][0]) == ('X', 'X', 'X'):
            xwin = True
            
        owin = False
        if (cells[0][0], cells[0][1], cells[0][2]) == ('O', 'O', 'O') or (cells[1][0], cells[1][1], cells[1][2]) == ('O', 'O', 'O') or (cells[2][0], cells[2][1], cells[2][2]) == ('O', 'O', 'O') \
        or (cells[0][0], cells[1][0], cells[2][0]) == ('O', 'O', 'O') or (cells[0][1], cells[1][1], cells[2][1]) == ('O', 'O', 'O') or (cells[0][2], cells[1][2], cells[2][2]) == ('O', 'O', 'O') \
        or (cells[0][0], cells[1][1], cells[2][2]) == ('O', 'O', 'O') or (cells[0][2], cells[1][1], cells[2][0]) == ('O', 'O', 'O'):
            owin = True
           
        if owin == True:
            print("O wins")
            break
        elif xwin == True:
            print("X wins")
            break
        elif (x_num + o_num) == 9 and not owin and not xwin:
            print("Draw")
            break
