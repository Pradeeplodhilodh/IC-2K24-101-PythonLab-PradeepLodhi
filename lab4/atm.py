balance = 5000
pin = "1234"

if input("PIN: ") == pin:
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
                print("Withdraw successful")
            else:
                print("Insufficient balance")

        elif c == "4":
            break
else:
    print("Wrong PIN")