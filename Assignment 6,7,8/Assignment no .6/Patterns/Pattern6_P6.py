#            1  
#         1  2  1
#      1  2  3  2  3
#   1  2  3  4  4  5  6
#1  2  3  4  5  7  8  9  10
num = 1
for i in range (1,6):
    for j in range(1,6-i):
        print(' ', end= "  ")
        
    for j in range(1, i+1):
        print(j,end="  ")
        
    for j in range(1,i):
        print(num,end ="  ")  
        num += 1  
        
    print()  