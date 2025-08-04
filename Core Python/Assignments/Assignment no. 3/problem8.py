#8. Write a program to prompt user to enter userid and password.
# After verifying userid and password display a 4 digit random number and ask user to enter the same.
# If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random

Username = "Harshali"
password = "pass@123"

Username =(input("Username: "))
password =(input("password: "))

if(Username == "Harshali" and password == "pass@123"):
    captcha = random.randint(1111 ,9999)
    print(f"Captcha:{captcha} ")
    user_captcha = int(input("Enter captcha: "))
    
    if(captcha == user_captcha):
        print("Captcha is correct , So it is succeefully login.")
    else:
        print("Captcha is not correct")
else:
    print("Captcha is worong ,  So it is unsuccessful to login")            


