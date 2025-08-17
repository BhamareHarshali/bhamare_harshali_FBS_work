#4. Sum of all odd numbers between 1 to n

def odd(num):
    total = 0
    #fuction body 
    for i in range(1 ,num+1):
        if i % 2 != 0:
            total += i
    return total        
num = int(input("Enter the n : "))
print("Sum of odd number: ",odd(num))