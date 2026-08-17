import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess a number between 1 and 100.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        print("Attempts:", attempts)
        break
else:
    print("You ran out of attempts.")
    print("The number was:", number)