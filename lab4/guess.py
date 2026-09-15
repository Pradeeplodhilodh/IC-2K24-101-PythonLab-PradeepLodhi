import random

n = random.randint(1, 100)
score = 100

for i in range(10):
    g = int(input("Guess: "))

    if g == n:
        print("Correct! Score:", score)
        break

    score -= 10

    if g < n:
        print("Too low")
    else:
        print("Too high")

    print("Even" if n % 2 == 0 else "Odd")
    print("Multiple of 5" if n % 5 == 0 else "Not multiple of 5")
else:
    print("You lost. Score: 0")