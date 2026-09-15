low = int(input("Low: "))
high = int(input("High: "))
count = 0

while low <= high:
    mid = (low + high) // 2
    count += 1

    print("My guess:", mid)
    x = input("h/l/c: ")

    if x == "c":
        print("Found in", count, "guesses")
        break
    elif x == "h":
        high = mid - 1
    elif x == "l":
        low = mid + 1