import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess > highest_num or guess < lowest_num:
            print("Invalid")
            print(
                f"please select a number between {lowest_num} amd {highest_num}")
        elif guess > answer:
            print("To low ! Try again!!")
        elif guess < answer:
            print("To highest ! Try again!!")
        else:
            print(f"CORRECT! The answer {guess}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")
        print(f"please select a number between {lowest_num} amd {highest_num}")
