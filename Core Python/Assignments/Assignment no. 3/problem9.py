#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

M1 = int(input("Enter marks of sunject 1: "))
M2 = int(input("Enter marks of sunject 2: "))
M3 = int(input("Enter marks of sunject 3: "))
M4 = int(input("Enter marks of sunject 4: "))
M5 = int(input("Enter marks of sunject 5: "))

total_marks = M1 + M2 + M3 + M4 + M5
percentage = total_marks /5

print(f'percentage : {percentage}')

if (percentage >= 95 ):
    print('Destinction.')
elif (percentage >= 85):
    print('First Class.')
elif (percentage >=75):
    print('Second Class.')
elif (percentage >=60):
    print('Pass.')
else:
    print('Fail')                
