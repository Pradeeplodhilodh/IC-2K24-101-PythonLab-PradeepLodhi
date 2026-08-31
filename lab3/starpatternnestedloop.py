n = int(input("Enter a number: "))

for row in range(1, n + 1):
    for star in range(row):
        print("*", end="")
    print()