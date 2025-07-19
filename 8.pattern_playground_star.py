#DIAMOND
def diamond():
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


#HILL PATTERN
def hill_pattern():       
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


#HORIZONTAL_DIAMOND
def horizontal_diamond():   
    # Upper part
    n = int(input("Enter size of half vertical diamond: "))
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
    # Lower part
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()


#LEFT ALIGNED TRIANGLE
def left_aligned_triangle():   
    n = int(input("Enter size of triangle :"))
    for i in range(n):
        for j in range(i +1):
            print(" ",end=" ")
        for j in range(i,n):
            print("*",end=" ")
        print()


#PYRAMID
def pyramid():   
    n = int(input("Enter size of triangle :"))
    for i in range(n):
        for j in range(i,n):
            print("",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()


#REVERSE HILL
def reverse_hill():   
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


#REVERSE LEFT TRIANGLE
def reverse_left_triangle():   
    n = int(input("Enter size of triangle pattern:"))
    for i in range(n):
        for j in range(i,n):
            print("*",end=" ")
        print()    


#REVERSE PYRAMID
def reverse_pyramid():   
    n = int(input("Enter size of triangle: "))
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")
        for j in range(2 * (n - i) - 1):
            print("*", end=" ")
        print()


#RIGHT ALIGNED TRIANGLE
def reverse_aligned_triangle():   
    n = int(input("Enter size of triangle :"))
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()


#RIGHT TRIANGLE
def right_triangle():  
        n = int(input("Enter size of triangle: ")) 
        for i in range(n): 
            for j in range(i+1):    
                print("*", end=" ")
            print()  


#SQUARE 
def square():
    n = int(input("Enter size of square: "))
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
       

patterns = {
    1: ("Diamond", diamond),
    2: ("Hill Pattern", hill_pattern),
    3: ("Horizontal Diamond", horizontal_diamond),
    4: ("Left Aligned Triangle", left_aligned_triangle),
    5: ("Pyramid", pyramid),
    6: ("Reverse Hill", reverse_hill),
    7: ("Reverse Left Triangle", reverse_left_triangle),
    8: ("Reverse Pyramid", reverse_pyramid),
    9: ("Right Aligned Triangle", reverse_aligned_triangle),
    10: ("Right Triangle", right_triangle),
    11: ("Square", square)
}


while True:
    print("\nChoose a pattern:")
    for key, value in patterns.items():
        print(f"{key}. {value[0]}")
    print("0. Exit")

    choice_input = input("Enter your choice: ").strip()
    if not choice_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    choice = int(choice_input)
    if choice == 0:
        print("Exiting...")
        break
    elif choice in patterns:
        patterns[choice][1]()
    else:
        print("Invalid choice! Try again.")