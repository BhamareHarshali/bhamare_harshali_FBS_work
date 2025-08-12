#4. Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter a number: "))
temp = num 
sum = 0

while temp > 0 :
    d = temp % temp 
    temp = temp // 10
    
if sum ==num :
    print(f'{num} is Amstrong number .')
else:
    print(f'{num} is not Amstrong number . ')            
    
    
    