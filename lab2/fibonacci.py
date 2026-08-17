# Loop version

n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci using loop:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Recursive version

calls = 0

def fibonacci(x):
    global calls
    calls += 1

    if x <= 1:
        return x

    return fibonacci(x - 1) + fibonacci(x - 2)


print("\n\nFibonacci using recursion:")

calls = 0

for i in range(n):
    print(fibonacci(i), end=" ")

print("\nFunction calls:", calls)