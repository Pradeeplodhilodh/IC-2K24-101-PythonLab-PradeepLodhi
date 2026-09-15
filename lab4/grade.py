marks = []

while True:
    print("1.Enter Marks 2.View Grade 3.Exit")
    c = input("Choice: ")

    if c == "1":
        marks = []
        for i in range(5):
            marks.append(float(input("Marks: ")))

    elif c == "2":
        if len(marks) == 5:
            a = sum(marks) / 5

            if a >= 90: g = "A"
            elif a >= 75: g = "B"
            elif a >= 60: g = "C"
            elif a >= 40: g = "D"
            else: g = "F"

            print("Average:", a, "Grade:", g)
        else:
            print("No data")

    elif c == "3":
        break