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
    pass

def display_hint(hint):
    pass

def display_ansewer(ansewer):
    pass


def main():
    pass

if __name__ == "__main__":
    main()
