def armstrong(n):
    temp = n
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10

    return total == n


n = int(input("Enter number: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not Armstrong number")

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Armstrong numbers:")
for i in range(start, end + 1):
    if armstrong(i):
        print(i, end=" ")