# triangle pattern
print("Triangle pattern:")

n = int(input("Enter size: "))
for i in range(n):
    for j in range(i + 1):
        print(" * ", end="")
    print()

