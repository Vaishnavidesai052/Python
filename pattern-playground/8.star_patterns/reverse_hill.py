#REVERSE HILL
n = int(input("Enter size of triangle: "))
for i in range(n):
    # Left triangle
    for j in range(i + 1):
        print("*", end=" ")

    # Middle spaces
    for j in range(2 * (n - i - 1)):
        print(" ", end=" ")

    # Right triangle
    for j in range(i + 1):
        print("*", end=" ")
    print()
