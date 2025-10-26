# han game

import random
#  dictionary of the key
from WordList  import word

hangman_key = {0: ("   ",
                   "   ",
                   "   ",),
               1: (" o ",
                   "   ",
                   "   ",),
               2: (" o ",
                   " | ",
                   "   ",),
               3: (" o ",
                   "/|",
                   "   ",),
               4: (" o ",
                   "/|\\",
                   "   ",),
               5: (" o ",
                   "/|\\",
                   "/ ",),
               6: (" o ",
                   "/|\\",
                   "/ \\",)}
# print(hangman_key[0])

# for line in hangman_key[6]:
#     print(line)


def display_man(wrong_guesses):
    print("*** Hangman *****")
    for line in hangman_key[wrong_guesses]:
        print(line)
    print("******************")


def display_hint(hint):
    print("Hint:   ", "  ".join(hint))


def display_answer(answer):
    print("answer: ", "  ".join(answer))


def main():
    answer = random.choice(word)
    # print(answer)
    hint = ["_"] * len(answer)
    # print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("INVALID INPUT")
            continue

        if not guess.isalpha():
            print("INVALID INPUT")
            continue
        
        if guess in  guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i].lower() == guess:
                    hint[i] = guess
        else :
             wrong_guesses += 1
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YPU WIN THE GAME")
            
            is_running = False
            
        elif wrong_guesses >= len(hangman_key) - 1 :
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE ")  
            is_running = False
            
if __name__ == "__main__":
    main()
