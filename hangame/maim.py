# han game

import random

word = ("apple", "banana", "orange", "grape", "mango", "peach", "cherry", "strawberry", "watermelon")


#  dictionary of the key
#
hangman_key = { 0: ("   ",
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
                    "/ \\",) }
# print(hangman_key[0])

# for line in hangman_key[6]:
#     print(line)


def display_man(wrong_guesses):
    print("*** Hangman *****")
    for line in hangman_key[wrong_guesses]:
        print(line)
    print("******************")

def display_hint(hint):
    print("Hint: ", " ".join(hint))

def display_ansewer(ansewer):
    print("The answer is: ", ansewer)


def main():
    ansewer = random.choice(word)
    # print(ansewer)
    hint = ["_"] * len(ansewer)
    # print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        dispaly_ansewer(ansewer)
        guess = input("Guess a letter: ").lower()
if __name__ == "__main__":
    main()
