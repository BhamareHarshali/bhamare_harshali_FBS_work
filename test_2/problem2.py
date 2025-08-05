#2.Write a program to accept 3 digit number. 
# If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
#Eg : - 428 , 214 etc.

num = int(input("Enter the 3-digit number: "))

if num >= 100 and num <= 999:
    a = num // 100        # First digit
    b = (num // 10) % 10  # Second digit
    c = num % 10          # Third digit

    if a == 2 * b and a * 2 == c:
        print("Yes, you have done it!")
    else:
        print("Please try next time.")
else:
    print("Please enter a 3-digit number.")
