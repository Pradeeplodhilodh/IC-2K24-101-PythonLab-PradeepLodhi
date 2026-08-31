n = int(input("Enter number of rows: "))

total_rows = 2 * n - 1
center = n - 1

for row in range(total_rows):

    distance = abs(center - row)

    stars = n - distance
    middle_spaces = 2 * distance

    for count in range(stars):
        print("*", end="")

    for count in range(middle_spaces):
        print(" ", end="")

    for count in range(stars):
        print("*", end="")

    print()