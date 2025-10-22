# python banking system

def show_balance(balance):
    print("____________________________________________")
    print("____________________________________________")
    print(f"  Your balance is ${balance:.2f}")
    print("_______________________vh______________________")



def deposit(balance):
    amount = float(input("Enter an amount to be deposited : "))

    if amount < 0:
        print("____________________________________________")
        print("  that is not valid amount")
        print("____________________________________________")
        return 0
    else:
        print("____________________________________________")
        print(f"  You successfully deposit ${amount:.2f}")
        print(f"  Your current balance is ${balance + amount: .2f}")
        print("____________________________________________")

        return amount


def withdraw(balance):
    amount = float(input("Enter amount to be withdraw : $"))
    if amount < 0:
        print("____________________________________________")
        print(f"  ${amount} is not valid amount in  our bank ")
        print("____________________________________________")
        return 0
    elif balance < amount:
        print("____________________________________________")
        print(f"  Your balance is insufficient to withdraw ${amount}")
        print("____________________________________________")

        return 0
    else:
        print("____________________________________________")

        print(f"  you successfully withdraw ${amount:.2f}")
        print(f"  Your current Balance is ${balance - amount: .2f}")
        print("____________________________________________")

        return amount


def main():

    balance = 0
    is_running = True

    while is_running:
        print("********************************************")
        print("              Banking program")
        print("____________________________________________")

        print("1, Show Banking")
        print("2, Deposit")
        print("3, Withdraw")
        print("4, Exit")
        print("********************************************")

        choice = int(input("Enter Your choice (1-4)  "))

        print("_____________________________________________")


        match choice:
            case 1 | "1":
                show_balance(balance)
            case 2 | "2":
                balance += deposit(balance)
            case 3 | "3":
                balance -= withdraw(balance)
            case 4 | "4":
                is_running = False
            case _:
                print("____________________________________________")

                print(f"  {choice} is wrong choice")
                print("  please select between  (1-4)")
                print("________________________________________")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("thank to you use our bank system")
    print("have a nice day")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


if __name__ == "__main__":
  main()
