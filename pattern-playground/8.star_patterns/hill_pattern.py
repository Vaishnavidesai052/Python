#HILL PATTERN
n = int(input("Enter size of triangle: "))
for i in range(n):
    for j in range(i, n - 1):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()
