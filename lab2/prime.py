def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = int(input("Enter number: "))

if prime(n):
    print("Prime number")
else:
    print("Not prime number")

limit = int(input("Enter limit: "))

print("Prime numbers:")
for i in range(2, limit + 1):
    if prime(i):
        print(i, end=" ")