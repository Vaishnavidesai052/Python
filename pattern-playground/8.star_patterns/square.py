#SQUARE 
def pattern(N):
    for i in range(N):
        for j in range(N):
            print("*",end=" ")
        print()
N=int(input("Enter size of square pattern: "))        
pattern(N)
        