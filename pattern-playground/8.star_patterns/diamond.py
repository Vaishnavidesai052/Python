#DIAMOND
n = int(input("Enter size of diamond: "))
# Upper half
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
# Lower half
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
