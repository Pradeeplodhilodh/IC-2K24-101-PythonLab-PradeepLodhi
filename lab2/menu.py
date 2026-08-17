# ---------- Armstrong ----------

def is_armstrong(n):
    if n < 0:
        return False

    digits = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n


def armstrong():
    n = int(input("Enter number: "))

    if n < 0:
        print("Enter a positive number")
        return

    if is_armstrong(n):
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    if start < 0 or end < 0 or start > end:
        print("Invalid range")
        return

    print("Armstrong numbers:")
    for i in range(start, end + 1):
        if is_armstrong(i):
            print(i, end=" ")

    print()


# ---------- Prime ----------

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def prime():
    n = int(input("Enter number: "))

    if is_prime(n):
        print("Prime number")
    else:
        print("Not a prime number")

    limit = int(input("Enter limit: "))

    print("Prime numbers:")
    for i in range(2, limit + 1):
        if is_prime(i):
            print(i, end=" ")

    print()


# ---------- Perfect ----------

def is_perfect(n):
    if n <= 0:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


def perfect():
    n = int(input("Enter number: "))

    if is_perfect(n):
        print("Perfect number")
    else:
        print("Not a perfect number")

    limit = int(input("Enter limit: "))

    print("Perfect numbers:")
    for i in range(1, limit + 1):
        if is_perfect(i):
            print(i, end=" ")

    print()


# ---------- Palindrome ----------

def number_palindrome(n):
    if n < 0:
        return False

    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10

    return original == reverse


def palindrome():
    n = int(input("Enter number: "))

    if number_palindrome(n):
        print("Palindrome number")
    else:
        print("Not a palindrome number")

    text = input("Enter string: ")

    if text == text[::-1]:
        print("Palindrome string")
    else:
        print("Not a palindrome string")


# ---------- Fibonacci ----------

def fibonacci_loop(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


calls = 0


def fibonacci_recursive(n):
    global calls

    calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci():
    global calls

    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Enter a positive number")
        return

    print("Using loop:")
    fibonacci_loop(n)

    calls = 0

    print("\nUsing recursion:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print("\nRecursive function calls:", calls)


# ---------- Patterns ----------

def patterns():
    n = int(input("Enter number of rows: "))

    if n <= 0:
        print("Enter a positive number")
        return

    # Star Triangle
    print("\nStar Triangle:")

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

    # Number Pattern
    print("\nNumber Pattern:")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Pyramid
    print("\nPyramid:")

    for i in range(1, n + 1):

        for j in range(n - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()


# ---------- Menu ----------

while True:

    print("\n========== MENU ==========")
    print("1. Armstrong Number")
    print("2. Prime Number")
    print("3. Perfect Number")
    print("4. Palindrome")
    print("5. Fibonacci Series")
    print("6. Pattern Printing")
    print("7. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice == "1":
        armstrong()

    elif choice == "2":
        prime()

    elif choice == "3":
        perfect()

    elif choice == "4":
        palindrome()

    elif choice == "5":
        fibonacci()

    elif choice == "6":
        patterns()

    elif choice == "7":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Please enter 1 to 7.")