# python slot machine
import random

# Game constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol weights for spinning
symbol_count = {
    "⭐": 2,
    "🔔": 4,
    "🍎": 6,
    "🍉": 8,
    "🍋": 10
}

# Payout multipliers for symbols
symbol_values = {
    "⭐": 10,
    "🔔": 7,
    "🍎": 5,
    "🍉": 4,
    "🍋": 3,
}


def check_winnings(columns, lines, bet, values):
    """
    Checks for winning lines and calculates the payout.
    Only horizontal lines are checked.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generates a random slot machine spin based on symbol weights.
    """
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Prints the slot machine grid.
    """
    print()
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
    print()


def deposit():
    """
    Prompts the user to deposit money into their balance.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    """
    Prompts the user for the number of lines to bet on.
    """
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    """
    Prompts the user for the bet amount per line.
    """
    while True:
        amount = input(
            f"What would you like to bet on each line (${MIN_BET}-${MAX_BET})? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def play_round(balance):
    """
    Executes a single round of the slot machine game.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"\nYou are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print("Spinning----\n")
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    if winnings > 0:
        print(f"You won ${winnings}!")
        if winning_lines:
            print(f"You won on line(s):", *winning_lines)
    else:
        print("Sorry, you didn't win this time.")

    return balance + winnings - total_bet


def main():
    """
    Main game loop.
    """
    print("********************************\n")
    print("   Welcome to Python Slots!   ")
    print("Symbols: ⭐ 🍉 🔔 🍎 🍋\n")
    print("********************************")

    balance = deposit()

    while True:
        print(f"\nCurrent balance is ${balance}")
        if balance < MIN_BET:
            print("You don't have enough money to place a bet.")
            break

        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance = play_round(balance)

    print("***********************************************\n")
    print(f"Game over! You left with ${balance}\n")
    print("***********************************************\n")


if __name__ == "__main__":
    main()
