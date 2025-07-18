#REVERSE PYRAMID
n = int(input("Enter size of triangle: "))
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()
