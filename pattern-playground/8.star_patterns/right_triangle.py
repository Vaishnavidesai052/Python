#RIGHT TRIANGLE
def printTriangle(N):
        for i in range(N): 
            for j in range(i+1):    
                print("*", end=" ")
            print()  
N=int(input("Enter size of triangle pattern: "))   
printTriangle(N)