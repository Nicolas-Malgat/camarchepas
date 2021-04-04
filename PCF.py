import random
import os
from time import sleep
from enum import Enum, unique

user_input = "> "

game_info = "#"
print_info = lambda *text: print('\t'.join(tuple(game_info) + text))

clear = lambda: os.system('cls')

@unique
class GameOutcome(Enum):
    TIE     = 0
    WIN     = 1
    LOOSE   = 2

@unique
class PrintColor(Enum):
    BLUE    = '\033[34m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    RESET   = '\033[0m'

@unique
class Choice(Enum):
    ROCK    = '1'
    PAPER   = '2'
    SCISSORS = '3'

def game_loop():
    print("Type q to quit anytime !\n")
    while True:
        game()
        print()
        if random.random() < 0.2:
            print("Type q to quit anytime !\n")

def game():
    user = user_choice()

    computer = computer_choice()
    
    print_info('Player: ', user.name.capitalize())
    print_info('Computer:', computer.name.capitalize())
    
    color, outcome = game_outcome(user, computer)

    print_info(color + outcome.name + PrintColor.RESET.value)
    sleep(0.5)
    clear()

def game_outcome(user, computer):
    if user == computer:
        return PrintColor.BLUE.value, GameOutcome.TIE
    elif is_win(user, computer):
        return PrintColor.GREEN.value, GameOutcome.WIN
    else:
        PrintColor.RED.value, GameOutcome.LOOSE

def user_choice():

    user = input_user('\n'.join(chc.value + ': ' + chc.name.capitalize() for chc in Choice), '\n')

    while user not in Choice._value2member_map_:
        user = input_user()

    return Choice(user)

def input_user(*text):
    try:
        user = input(''.join(text + tuple(user_input)))
    except (KeyboardInterrupt, EOFError):
        print()
        exit_game()

    if user in ['q', 'Q']:
        exit_game()

    return user

def exit_game():
    word = "Goodbye"
    length_word = len(word) + 1
    for nb_let in range(length_word):
        print (word[:nb_let], end="\r")
        sleep(random.randrange(10, 100, 10)/1000)
    # print(' '*length_word, end='\r')

    exit(0)

def computer_choice():
    computer_thinking()

    return random.choice(list(Choice))

def computer_thinking():
    for nb_dot in range (0, 4):
        print ("." * nb_dot, end="\r")
        sleep(random.randrange(50, 100, 10)/1000)
    print('   ', end='\r')

def is_win(A, B):
    if      (A == Choice.ROCK       and B == Choice.SCISSORS) \
        or  (A == Choice.SCISSORS   and B == Choice.PAPER) \
        or  (A == Choice.PAPER      and B == Choice.ROCK):
        return True
    return False

if __name__ == "__main__":
    game_loop()
