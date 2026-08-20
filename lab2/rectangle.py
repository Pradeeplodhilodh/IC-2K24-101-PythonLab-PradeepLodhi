# Rectangle pattern
print("Rectangle pattern:")
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

for i in range(n):
    for j in range(m):
        print(" * ", end="")
    print()

