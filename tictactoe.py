import random
import time
import os

gameBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

boardKeys = []

for key in gameBoard:
    boardKeys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def numbers():
    print('7|8|9')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('1|2|3')

def api(gameBoard):
    avaliable = []

    for key in gameBoard:
        if gameBoard[key] == ' ':
            avaliable.append(key)
    
    ran = random.choice(avaliable)
    return ran

def checkNumberX(gameBoard, number1, number2, number3):
    taken = []

    for key in gameBoard:
        if gameBoard[key] == 'X':
            taken.append(key)
    
    if number1 in taken and number2 in taken:
        if number3 not in taken and gameBoard[number3] != 'O': return True
        else: return False

def checkNumberO(gameBoard, number1, number2, number3):
    taken = []

    for key in gameBoard:
        if gameBoard[key] == 'O':
            taken.append(key)

    if number1 in taken and number2 in taken:
        if number3 not in taken and gameBoard[number3] != 'X': return True
        else: return False

def advanceAPI(gameBoard):

    if checkNumberO(gameBoard, '1', '2', '3') == True:
        return '3'
    if checkNumberO(gameBoard, '2', '3', '1') == True:
        return '1'
    if checkNumberO(gameBoard, '5', '6', '4') == True:
        return '4'
    if checkNumberO(gameBoard, '4', '5', '6') == True:
        return '6'
    if checkNumberO(gameBoard, '4', '6', '5') == True:
        return '3'
    if checkNumberO(gameBoard, '7', '8', '9') == True:
        return '9'
    if checkNumberO(gameBoard, '7', '9', '8') == True:
        return '8'
    if checkNumberO(gameBoard, '9', '8', '7') == True:
        return '7'
    if checkNumberO(gameBoard, '7', '5', '3') == True:
        return '3'
    if checkNumberO(gameBoard, '7', '3', '5') == True:
        return '5'
    if checkNumberO(gameBoard, '3', '5', '7') == True:
        return '7'
    if checkNumberO(gameBoard, '9', '1', '5') == True:
        return '5'
    if checkNumberO(gameBoard, '1', '5', '9') == True:
        return '9'
    if checkNumberO(gameBoard, '5', '9', '1') == True:
        return '1'
    if checkNumberO(gameBoard, '9', '6', '3') == True:
        return '3'
    if checkNumberO(gameBoard, '9', '3', '6') == True:
        return '6'
    if checkNumberO(gameBoard, '3', '6', '9') == True:
        return '9'

    if checkNumberX(gameBoard, '1', '2', '3') == True:
        return '3'
    if checkNumberX(gameBoard, '2', '3', '1') == True:
        return '1'
    if checkNumberX(gameBoard, '5', '6', '4') == True:
        return '4'
    if checkNumberX(gameBoard, '4', '5', '6') == True:
        return '6'
    if checkNumberX(gameBoard, '4', '6', '5') == True:
        return '3'
    if checkNumberX(gameBoard, '7', '8', '9') == True:
        return '9'
    if checkNumberX(gameBoard, '7', '9', '8') == True:
        return '8'
    if checkNumberX(gameBoard, '9', '8', '7') == True:
        return '7'
    if checkNumberX(gameBoard, '7', '5', '3') == True:
        return '3'
    if checkNumberX(gameBoard, '7', '3', '5') == True:
        return '5'
    if checkNumberX(gameBoard, '3', '5', '7') == True:
        return '7'
    if checkNumberX(gameBoard, '9', '1', '5') == True:
        return '5'
    if checkNumberX(gameBoard, '1', '5', '9') == True:
        return '9'
    if checkNumberX(gameBoard, '5', '9', '1') == True:
        return '1'
    if checkNumberX(gameBoard, '9', '6', '3') == True:
        return '3'
    if checkNumberX(gameBoard, '9', '3', '6') == True:
        return '6'
    if checkNumberX(gameBoard, '3', '6', '9') == True:
        return '9'
    
    return api(gameBoard)
    
    
def game():
    turn = 'X'
    count = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    plr1 = input("Please enter player 1's name: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    plr2 = input("Please enter player 2's name: ")
    os.system('cls' if os.name == 'nt' else 'clear')
        

    for i  in range(10):
        if count == 0:
            numbers()
        else:
            printBoard(gameBoard)
        
        if turn == 'O' and plr2 == 'api' or turn == 'O' and plr2 == 'API': 
            print("API is thinking...")
            time.sleep(1.5)
            move = advanceAPI(gameBoard)
        else:
            move = input(turn + ' it\'s your turn: ')

        if int(move) < 1 or int(move) > 9:
            print("Invalid number choice!")
            continue

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('That place is already filled!')
            continue

        if count >= 5:
            winner = str
            if turn == 'X':
                winner = plr1
            else:
                winner = plr2

            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("****** Game Over ******\n")
                print("****** " + winner + " you win ******")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("****** Game Over ******\n")
                print("****** " + winner + " you win ******")
                break
            elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("****** Game Over ******\n")
                print("****** " + winner + " you win ******")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("***Game Over***  ******\n")
                print("****** " + winner + " you win ******")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("****** Game Over ******\n")
                print("****** " + winner + " you win ******")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("****** Game Over ******\n")
                print("****** " + winner + " you win ******")
                break
            elif gameBoard['3'] == gameBoard['5'] == gameBoard['7'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("****** Game Over ******\n")
                print("****** " + winner + " you win ******")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] == turn:
                os.system('cls' if os.name == 'nt' else 'clear')
                printBoard(gameBoard)
                print("****** Game Over ******\n")
                print("****** " + winner + " you win ******")
                break
        
        if count == 9:
            printBoard(gameBoard)
            print("****** Game Over ******\n")
            print("****** It's a tie ******") 
            break
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    restart = input("Do you want to restart? (Y/N) ")
    if restart == 'Y' or restart == 'y':
        for key in boardKeys:
            os.system('cls' if os.name == 'nt' else 'clear')
            gameBoard[key] = ' '
        game()

if __name__ == "__main__":
    game()