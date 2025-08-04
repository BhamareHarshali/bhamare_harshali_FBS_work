#2. Write a program to input any alphabet and check whether it is vowel or consonant.

alpha =(input("Enter the alphabets:"))
if(alpha in "aeiou AEIOU"):
    print(f'vowels:{alpha}')
else:
    print(f'Consonat')  