students = {}

while True:
    name = input("Enter student name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        break
    math = int(input("Enter Math score: "))
    science = int(input("Enter Science score: "))
    students[name] = {"Math": math, "Science": science}

print("\nStudent Report:")
for student, subjects in students.items():
    avg = (subjects["Math"] + subjects["Science"]) / 2
    status = "Pass" if avg >= 40 else "Fail"
    print(f"{student} -> Math: {subjects['Math']}, Science: {subjects['Science']}, Avg: {avg}, Status: {status}")
