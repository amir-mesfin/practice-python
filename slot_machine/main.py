# python slot machine
import random
def spin_row():
    symbols = ['⭐', '🍉', '🔔', '🍎', '🍋']
    
    return [random.choice(symbols) for _ in range(3)]
    

def print_row(row):
    print("*****************")
    print("  |  ".join(row))
    print("*****************")
     


def get_payment():
    pass


def main():
    balance = 100
    print("*****************************************")
    print("Welcome to python Slot ")
    print("Symbols: ⭐ 🍉 🔔 🍎 🍋")
    print("****************************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("place Your bet amount")
        if not bet.isdigit():
            print("please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <= 0:
            print("bet must be grater than zero")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning----\n")
        print_row(row)
if __name__ == "__main__":
    main()
