# python slot machine
import random
def spin_row():
    symbols = ['⭐', '🍉', '🔔', '🍎', '🍋']

    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("*****************\n")
    print("  |  ".join(row),"\n")
    print("******************")


def get_payment(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case '🍉':
                return bet * 3
            case '🍎':
                return bet * 4
            case '🍋':
                return bet * 5
            case  '🔔':
                return bet * 7
            case  '⭐':
                return bet * 10
            case _:
                return 0
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return bet

    else:
        return 0


def main():
    balance = 100
    print("********************************\n")
    print("Welcome to python Slot ")
    print("Symbols: ⭐ 🍉 🔔 🍎 🍋\n")
    print("*********************************")

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

        payout = get_payment(row, bet)
        if payout > 0:
            print(f" you won ${payout}")
            print(f"Your balance is ${balance + bet}")
        else:
            print("Sorry you Loose")

        balance += payout
        play_again = input(" Do you want to spin again ?  (y/n)").lower()
        if not play_again == 'y':
            break

    print("***********************************************\n")
    print(f"game over Your final balance is ${balance}\n")
    print("***********************************************\n")


if __name__ == "__main__":
    main()
