#2. Enter number of students from user. 
# For those many students accept marks of 5 subject marks from user and calculate percentage. 
# Display all percentage and average percentage of students.

num_students = int(input("Enter the number of students : "))


percentage = []

for student in range(1 , num_students + 1):
    print(f"\n Enter marks for student {student}:")
    total_marks = 0
    
    for subject in range(1,6):
        marks = float(input(f'Subject {subject} marks: '))
        total_marks += marks
        
        percentage = total_marks / 500 * 100
        
for i in range(num_students):
    print(f"Student Percentage is :{percentage}.")

        
         