from time import sleep
board=['1','2','3','4','5','6','7','8','9']
turn1=True
turn2=False
draw=False
select = 0
p1win=False
p2win=False
name1=''
name2=''
score1=0
score2=0
play=False
playInput=''

def welcome():
    global name1, name2
    print("\t\t\tWelcome To Tic Tac Toe")
    sleep(0.5)
    name1 = input("Player 1 please enter your name : ").upper()
    sleep(0.5)
    name2 = input("Player 2 please enter your name : ").upper()
    sleep(1)
    print("Welcome ", name1, "And", name2)

def playAgain():
    global play, playInput, p1win, p2win, score1, score2, name1, name2
    print(name1, "Score -->", score1)
    print(name2, "Score -->", score2)
    while True:
        playInput=input("Do you want to play again(Y/N)").upper()
        if playInput == 'Y':
            play=True
            p1win=False
            p2win=False
            break
        if playInput == 'N':
            play=False
            break
        else:
            print("Enter correct choice")

def displayBoard():
    global select,turn1, turn2, choice, board
    print(board[0] , '|' , board[1] , '|' , board[2])
    print(board[3] , '|' , board[4] , '|' , board[5])
    print(board[6] , '|' , board[7] , '|' , board[8])

def resetBoard():
    global board
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def changeTurn():
    global select,turn1,turn2,choice,board
    if turn1==True:
        turn1=False
        turn2=True
    elif turn2==True:
        turn2=False
        turn1=True
def checkWin():
    global p1win,p2win,select,turn1, turn2, choice, board, score1, score2, name1, name2

    if board[0] == 'X' and board[1] == 'X' and board [2] == 'X' or board[3] =='X' and board[4] == 'X' and board [5] == 'X' or board[6] == 'X' and board[7] == 'X' and board [8] == 'X':
        print(name1," wins")
        p1win=True
    elif board[0] == 'X' and board[4] == 'X' and board [8] == 'X' or board[2] == 'X' and board[4] =='X' and board [6] == 'X':
        print(name1," wins")
        p1win=True
    elif board[0] == 'X' and board[3] == 'X' and board [6] == 'X' or board[1] == 'X' and board[4] == 'X' and board [7] == 'X' or board[2] == 'X' and board[5] == 'X' and board [8] == 'X':
        print (name1, " wins")
        p1win=True

    if board[0] == 'Y' and board[1] == 'Y' and board [2] == 'Y' or board[3] =='Y' and board[4] == 'Y' and board [5] == 'Y' or board[6] == 'Y' and board[7] == 'Y' and board [8] == 'Y':
        print(name2, " wins")
        p2win=True
    elif board[0] == 'Y' and board[4] == 'Y' and board [8] == 'Y' or board[2] == 'Y' and board[4] =='Y' and board [6] == 'Y':
        print(name2, " wins")
        p2win=True
    elif board[0] == 'Y' and board[3] == 'Y' and board [6] == 'Y' or board[1] == 'Y' and board[4] == 'Y' and board [7] == 'Y' or board[2] == 'Y' and board[5] == 'Y' and board [8] == 'Y':
        print (name2, " wins")
        p2win=True

def checkDraw():
    global draw, p1win, p2win, select, turn1, turn2, choice, board
    if board[0] != '1' and board[1] != '2' and board[2] != '3' and board[3] != '4' and board[4] != '5' and board[5] != '6' and board[6] != '7' and board[7] != '8' and board[8] != '9':
        draw=True


def selectBox1():
    global select, turn1, turn2, choice, board, name1
    print(name1, " enter your choice : ")
    select=int(input())

    if board[select - 1] != 'X' and board[select - 1] != 'Y':
        if select == 1:
            board [0] = 'X'

        elif select == 2:
            board [1] = 'X'

        elif select == 3:
            board [2] = 'X'

        elif select == 4:
            board [3] = 'X'

        elif select == 5:
            board [4] = 'X'

        elif select == 6:
            board [5] = 'X'

        elif select == 7:
            board [6] = 'X'

        elif select == 8:
            board [7] = 'X'

        elif select == 9:
            board [8] = 'X'
    else:
        print("Box Already Selected, Try Again")
        return selectBox1()


def selectBox2():
    global select, turn1, turn2, choice, board, name2
    print(name2, " enter your choice : ")
    select = int(input())
    if board[select-1] != 'X' and board[select-1] != 'Y':
        if select == 1:
            board[0] = 'Y'

        elif select == 2:
            board[1] = 'Y'

        elif select == 3:
            board[2] = 'Y'

        elif select == 4:
            board[3] = 'Y'

        elif select == 5:
            board[4] = 'Y'

        elif select == 6:
            board[5] = 'Y'

        elif select == 7:
            board[6] = 'Y'

        elif select == 8:
            board[7] = 'Y'

        elif select == 9:
            board[8] = 'Y'
    else:
        print("Box Already Selected, Try Again")
        return selectBox2()

welcome()
while True:
    play=False
    displayBoard()
    if turn1==True:
        sleep(1)
        selectBox1()
        checkWin()
        checkDraw()
        if draw==True:
            displayBoard()
            print("Draw")
            break
        if p1win==True:
            displayBoard()
            score1+=1
            playAgain()
            if play==True:
                resetBoard()
                continue
            break
        changeTurn()
    elif turn2==True:
        sleep(1)
        selectBox2()
        checkWin()
        if draw==True:
            displayBoard()
            print("Draw")
            sleep(4)
            playAgain()
            if play == True:
                resetBoard()
                continue
            break
        if p2win==True:
            displayBoard()
            score2+=1
            playAgain()
            if play == True:
                resetBoard()
                continue
            break
        changeTurn()
