n = int(input("Enter an odd number: "))

mid = n // 2

for row in range(n):

    distance = abs(mid - row)

    # Space before star
    for space in range(distance):
        print(" ", end="")

    print("*", end="")

    # Space between stars
    inside = 2 * (mid - distance) - 1

    if inside > 0:
        for space in range(inside):
            print(" ", end="")
        print("*", end="")

    print()