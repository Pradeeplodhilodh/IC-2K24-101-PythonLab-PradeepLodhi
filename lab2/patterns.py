n = int(input("Enter number of rows: "))

print("\nStar Pattern:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\nNumber Pattern:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("\nPyramid Pattern:")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()