def perfect(n):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    return total == n


n = int(input("Enter number: "))

if perfect(n):
    print("Perfect number")
else:
    print("Not perfect number")

limit = int(input("Enter limit: "))

print("Perfect numbers:")
for i in range(1, limit + 1):
    if perfect(i):
        print(i, end=" ")