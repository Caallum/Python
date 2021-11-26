import random

options = ['rock', 'paper', 'scissors']

while True:
    choice = input("Please enter your input: (r/p/s) (rock/paper/scissors) ")

    if choice == 'r' or choice == 'R' or choice == 'p' or choice == 'P' or choice == 's' or choice == 'S' or choice == 'rock' or choice == 'ROCK' or choice == 'PAPER' or choice == 'paper' or choice == 'scissors' or choice == 'SCISSORS':
        break

computerChoice = random.choice(options)

while computerChoice == choice:
    computerChoice = random.choice(options)

def checkAnswer(answ1, answ2):
    ans1 = answ1.lower()
    ans2 = answ2.lower()

    answer = ans1
    if ans1 == 'paper' and ans2 == 'rock':
        answer = ans1
    elif ans1 == 'scissors' and ans2 == 'paper':
        answer = ans1
    elif ans1 == 'rock' and ans2 == 'scissors':
        answer = ans1
    elif ans1 == 'paper' and ans2 == 'r':
        answer = ans1
    elif ans1 == 'scissors' and ans2 == 'p':
        answer = ans1
    elif ans1 == 'rock' and ans2 == 's':
        answer = ans1


    return answer

answ = checkAnswer(computerChoice, choice)
print(answ + " wins!")