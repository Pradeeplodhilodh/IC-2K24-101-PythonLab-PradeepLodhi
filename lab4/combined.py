import random

def atm():
    balance = 5000

    while True:
        print("1.Balance 2.Deposit 3.Withdraw 4.Exit")
        c = input("Choice: ")

        if c == "1":
            print(balance)
        elif c == "2":
            balance += float(input("Amount: "))
        elif c == "3":
            x = float(input("Amount: "))
            if x <= balance:
                balance -= x
            else:
                print("Insufficient balance")
        elif c == "4":
            break


def grade():
    m = [float(input("Marks: ")) for i in range(5)]
    a = sum(m) / 5

    if a >= 90: print("A")
    elif a >= 75: print("B")
    elif a >= 60: print("C")
    elif a >= 40: print("D")
    else: print("F")


def game():
    n = random.randint(1, 100)

    for i in range(10):
        g = int(input("Guess: "))

        if g == n:
            print("Correct")
            return

        print("Too low" if g < n else "Too high")

    print("You lost")


while True:
    print("1.ATM 2.Grade 3.Game 4.Exit")
    c = input("Choice: ")

    if c == "1": atm()
    elif c == "2": grade()
    elif c == "3": game()
    elif c == "4": break