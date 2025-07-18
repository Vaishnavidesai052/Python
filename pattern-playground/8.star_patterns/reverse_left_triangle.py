#REVERSE LEFT TRIANGLE
n = int(input("Enter size of triangle pattern:"))
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()    