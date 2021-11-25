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
 
def game():
    turn = 'X'
    count = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    plr1 = input("Please enter player 1's name: ")
    plr2 = input("Please enter player 2's name: ")
        

    for i  in range(10):
        if count == 0:
            numbers()
        else:
            printBoard(gameBoard)
        
        if turn == 'O' and plr2 == 'api' or turn == '0' and plr2 == 'API': 
            print("API is thinking...")
            time.sleep(1.5)
            move = api(gameBoard)
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