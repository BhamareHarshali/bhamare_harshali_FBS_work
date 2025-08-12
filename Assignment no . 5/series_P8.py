#8. Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
#e. x - x2/3 + x3/5 - x4/7 + .... to n terms

print("Choose a series to calculate:")
print("1. 1! + 2! + 3! + ... + n!")
print("2. N + N^2 + N^3 + ... + N^N")
print("3. Geometric series (ratio = 2)")
print("4. S = a + a²/2 + a³/3 + ... + a¹⁰/10")
print("5. x - x²/3 + x³/5 - x⁴/7 + ... up to n terms")


choice = int(input("Enter the number: "))

if choice == 1:
    num = int(input("Enter the fact value: "))

    i = 1
    fact = 1 
    while(i <= num):
        fact *= i  # fact =fact * i
        i +=1
    print(f'Factorial of {num} is {fact}.')

elif choice == 2  :
    num = int(input("Enter the N: "))
    total = 0
    for i in range(1,num+1):
        total += num ** i
    print("sum= ",total)    
    
elif choice == 3:
    num = int(input("Enter number of term: "))
    total = 0 
    for i in range(num):
        total += 2 ** i
    print("Sum = ",total)    
        
elif choice == 4:
    num = int(input("Enter value : "))
    total =0 
    for i in range (1,11):
        total += num ** i / i
    print("Sum= ",total)  

elif choice == 5:
    x = int(input("Enter the value of x :  ")) 
    num = int(input("Enter the number of term :  ")) 
    
    sum = 0
    term = 1
    
    for i in range(1,num+1):
        a = (x ** i )/(2 * i- 1)
        sum += term * a
        term *= -1
    print("Sum= ",sum)     
      
     


 
    