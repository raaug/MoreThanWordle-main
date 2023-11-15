import random
from wordlist import wordlist
from solutions import solutions

MAXIMUM_GUESSES = 6
NUMBER_OF_LETTERS = 5
BG_GREEN = "\u001b[42m"
BG_YELLOW = "\u001b[43m"
RESET = "\u001b[0m"
FG_BLACK = "\u001b[32m"



def process_guess(the_answer, the_guess):
    clue = ['-', '-', '-', '-', '-']
    answer_flag = [False, False, False, False, False]

    # Exact match loop
    for i, _ in enumerate(the_answer):
        if the_guess[i] == the_answer[i]:
            clue[i] = 'G'
            answer_flag[i] = True
    
    # Present, but out of position loop
    for i, _ in enumerate(the_guess):
        if clue[i] == '-': # No exact match from first loop
            for j, _ in enumerate(the_answer):
                if the_guess[i] == the_answer[j] and not answer_flag[j]:
                    clue[i] = 'Y'
                    answer_flag[j] = True
                    break # End the loop
    return clue


def game():
    # choose a word
    answer = random.choice(solutions)

    guess_count = 0
    correct_guess = False
    while guess_count < MAXIMUM_GUESSES and not correct_guess:
        guess = input('input 5 letter word and hit enter: ')
        if guess not in wordlist:
            print(f'{guess} not a valid word')
            continue
        guess_count += 1
        print(f'guess # {guess_count}')
        print('')
        clue = process_guess(answer, guess)
        for i, _ in enumerate(guess):
            if clue[i] == 'G':
                print(f"{BG_GREEN}{guess[i].upper()}{RESET}", end=" ")
            elif clue[i] == "Y":
                print(f"{FG_BLACK}{BG_YELLOW}{guess[i].upper()}{RESET}", end=" ")
            else:
                print(guess[i].upper(), end=" ")
        print()
    #    for i, _ in enumerate(guess):
    #        print(clue[i], end = " ")
    #    print()
        if answer == guess:
            print ("YOU WIN!")
            exit()
        elif guess_count == MAXIMUM_GUESSES:
            print(f'Sorry, the word was {answer}')
