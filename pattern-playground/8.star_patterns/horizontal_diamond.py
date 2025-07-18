n = int(input("Enter size of half vertical diamond: "))
# Upper part
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
# Lower part
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()