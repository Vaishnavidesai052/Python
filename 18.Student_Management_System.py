class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Course  : {self.course}")
        print("-" * 30)


# Class to manage multiple students
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, course):
        student = Student(name, roll_no, course)
        self.students.append(student)
        print("✅ Student added successfully!\n")

    def view_students(self):
        if not self.students:
            print("⚠️ No students to display.\n")
        else:
            print("📋 List of Students:\n")
            for student in self.students:
                student.display()

    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("🗑️ Student deleted successfully!\n")
                return
        print("❌ Student not found.\n")


# Main program
def main():
    manager = StudentManager()

    while True:
        print("\n====== Student Management Menu ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            roll_no = input("Enter roll number: ")
            course = input("Enter course: ")
            manager.add_student(name, roll_no, course)

        elif choice == '2':
            manager.view_students()

        elif choice == '3':
            roll_no = input("Enter roll number to delete: ")
            manager.delete_student(roll_no)

        elif choice == '4':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❗ Invalid choice. Please enter 1–4.\n")


# Run the program
main()
