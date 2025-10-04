#4. Create a class College which has collection of students.
# Add the following methods :
#a. Parameteried constructor for number of students.
#b. AddStudent
#c. GetStudent
#d. RemoveStudent
#e. Override __str__ Method

from Student import Student

class College:
    def __init__(self, max_std=0):
        # max number of students allowed in the college
        self.M_S = max_std
        self.Students = []   # list of Student (or derived class) objects

    # Add student object
    def addStudent(self, student: Student):
        if len(self.Students) < self.M_S:
            self.Students.append(student)
            print(f"Student {student.nm} added successfully.")
        else:
            print("Cannot add more students. College is full!")

    # Get student by ID
    def getStudent(self, student_id):
        for s in self.Students:
            if s.std_id == student_id:
                return s
        return None

    # Remove student by ID
    def removeStudent(self, student_id):
        for s in self.Students:
            if s.std_id == student_id:
                self.Students.remove(s)
                print(f"Student {s.nm} removed successfully.")
                return
        print("Student not found.")

    # String representation of College (all students)
    def __str__(self):
        if not self.Students:
            return "No students in the college."
        return "\n\n".join(str(s) for s in self.Students)


# ===============================
# Example Usage
# ===============================

if __name__ == "__main__":
    from EnggStudent import EnggStudent
    from MedicalStudent import MedicalStudent

    # Create college with capacity of 3 students
    c1 = College(3)

    # Create students
    s1 = Student(101, "Riya", 20, 82)
    s2 = EnggStudent(102, "Amit", 21, 75, "Computer", 80)
    s3 = MedicalStudent(103, "Sneha", 22, 78, "Cardiology", 88)

    # Add them to college
    c1.addStudent(s1)
    c1.addStudent(s2)
    c1.addStudent(s3)

    # Print all students
    print("\nCollege Students List:")
    print(c1)

    # Get one student
    print("\nGet Student with ID 102:")
    print(c1.getStudent(102))

    # Remove one student
    c1.removeStudent(101)

    print("\nAfter Removal:")
    print(c1)
