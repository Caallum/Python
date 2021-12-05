import random

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